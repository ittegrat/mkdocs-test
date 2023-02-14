from os import makedirs, path
from jinja2 import Environment, FileSystemLoader
from mkdocs.exceptions import PluginError
from mkdocs.structure.files import File
from mkdocs.utils import get_markdown_title, meta

def on_files(files, **kwargs):

  cfg = kwargs['config']
  tags = {}

  for file in filter(lambda f: f.is_documentation_page(), files):

    with open(file.abs_src_path, encoding='utf-8') as handle:

      body, head = meta.get_data(handle.read())

      if 'tags' not in head:
        continue

      head['src_uri'] = file.src_uri

      if 'title' not in head:
        head['title'] = get_markdown_title(body)

      ht = head['tags']
      if isinstance(ht, list):
        for t in ht:
          heads = tags.get(t, [])
          heads.append(head)
          tags[t] = heads
      elif isinstance(ht, str):
        heads = tags.get(ht, [])
        heads.append(head)
        tags[ht] = heads
      else:
        msg = f"Error in '{file.src_uri}': tags must be a string or a list."
        raise PluginError(msg)

  environment = Environment(
    loader=FileSystemLoader(path.join(path.dirname(__file__)))
  )
  template = environment.get_template('tags.md.template')

  folder = path.abspath(path.join(cfg["docs_dir"], '..', 'temp'))
  makedirs(folder, exist_ok=True)

  tags = sorted(tags.items(), key=lambda t: t[0].lower())

  with open(path.join(folder, 'tags.md'), "w", encoding='utf-8') as oname:
    oname.write(template.render(tags=tags))

  newfile = File(
    path=str('tags.md'),
    src_dir=str(folder),
    dest_dir=cfg["site_dir"],
    use_directory_urls=False
  )
  files.append(newfile)

def on_nav(nav, **kwargs):
  for i, item in enumerate(nav):
    if item.is_page and item.file.src_uri == 'tags.md':
      nav.items.insert(1, nav.items.pop(i))
      break

def on_page_markdown(markdown, page, **kwargs):
  tags = page.meta.get('tags')
  if tags is not None:
    if isinstance(tags, str): tags = [ tags ]
    links = [ f'[{t}](tags.md#{t}){{.button}}' for t in tags ]
    markdown = markdown.replace('{{TAGS}}', ' '.join(links))
  return markdown
