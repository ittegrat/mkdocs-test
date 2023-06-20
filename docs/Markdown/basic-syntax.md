---
tags: syntax
---
# Basic Syntax

## Headings

Markdown|Rendered Output
--------|---------------
`# Heading level 1`{: .md } | <h1>Heading level 1<h1>
`## Heading level 2`{: .md } | <h2>Heading level 2<h2>
`### Heading level 3`{: .md } | <h3>Heading level 3<h3>
`#### Heading level 4`{: .md } | <h4>Heading level 4<h4>
`##### Heading level 5`{: .md } | <h5>Heading level 5<h5>
`###### Heading level 6`{: .md } | <h6>Heading level 6<h6>


## Paragraphs

```markdown
I really like using Markdown.

I think I'll use it to format
all of my documents from now
on.
```

I really like using Markdown.

I think I'll use it to format
all of my documents from now
on.


## Line Breaks

```markdown
This is the first line.<br>
And this is the second line.
```

This is the first line.<br>
And this is the second line.


## Emphasis

### Bold

Markdown|Rendered Output
--------|---------------
`I just love **bold text**.`{: .md } | I just love **bold text**.
`I just love __bold text__.`{: .md } | I just love __bold text__.
`Love**is**bold`{: .md }             | Love**is**bold

### Italic

Markdown|Rendered Output
--------|---------------
`Italicized text is the *cat's meow*.`{: .md } | Italicized text is the *cat's meow*.
`Italicized text is the _cat's meow_.`{: .md } | Italicized text is the _cat's meow_.
`A*cat*meow`{: .md }                           | A*cat*meow

### Bold and Italic

Markdown|Rendered Output
--------|---------------
`This text is ***really important***.`{: .md } | This text is ***really important***.
`This text is ___really important___.`{: .md } | This text is ___really important___.
`This text is __*really important*__.`{: .md } | This text is __*really important*__.
`This text is **_really important_**.`{: .md } | This text is **_really important_**.
`This is really***very***important text.`{: .md } | This is really***very***important text.

## Blockquotes

```markdown
 > Dorothy followed her through many of the beautiful rooms in her castle.
```
> Dorothy followed her through many of the beautiful rooms in her castle.

```markdown
 > Dorothy followed her through many of the beautiful rooms in her castle.
The Witch bade her clean the pots and kettles and sweep the floor and keep
the fire fed with wood.
```
 > Dorothy followed her through many of the beautiful rooms in her castle.
The Witch bade her clean the pots and kettles and sweep the floor and keep
the fire fed with wood.

```markdown
 > Dorothy followed her through many of the beautiful rooms in her castle.
 >> The Witch bade her clean the pots and kettles and sweep the floor and keep
the fire fed with wood.
```
> Dorothy followed her through many of the beautiful rooms in her castle.
>> The Witch bade her clean the pots and kettles and sweep the floor and keep
the fire fed with wood.

```markdown
 > #### The quarterly results look great!
 >
 > - Revenue was off the chart.
 > - Profits were higher than ever.
 >
 >  *Everything* is going according to **plan**.
```

> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.


## Lists

### Unordered Lists

```markdown
 - First item
 * Second item
 + Third item
    - Indented item
        - Indented item
```
 - First item
 * Second item
 + Third item
    - Indented item
        - Indented item

### Ordered Lists

```markdown
 1. First item
 1. Second item
 1. Third item
    2. Indented item
        3. Indented item
```
 1. First item
 1. Second item
 1. Third item
    2. Indented item
        3. Indented item


## Links

###### With text
```markdown
A search engine is [Duck Duck Go](https://duckduckgo.com).
```
A search engine is [Duck Duck Go](https://duckduckgo.com).

###### With tooltip
```markdown
A search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine").
```
A search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine").

###### Simple links
```markdown
<https://github.com>
```
<https://github.com>

```markdown
<user@example.com>
```
<user@example.com>

###### Reference-style links
```markdown
[GitHub][gh_link_label]

[gh_link_label]: https://github.com 'GitHub Tooltip'
```
[GitHub][gh_link_label]

[gh_link_label]: https://github.com 'GitHub Tooltip'

###### Links to pages
```markdown
See the [extended syntax](extended-syntax.md) section.
```
See the [extended syntax](extended-syntax.md) section.

###### Anchor links
```markdown
See the section on [`emphasis`](#emphasis).
```
See the section on [`emphasis`](#emphasis).


## Images

### Image
```markdown
![Tux, the Linux mascot](https://www.markdownguide.org/assets/images/tux.png)
```
![Tux, the Linux mascot](https://www.markdownguide.org/assets/images/tux.png)

### Image Link
```markdown
[![Octocat](https://avatars.githubusercontent.com/u/583231)](https://octodex.github.com/)
```
[![Octocat](https://avatars.githubusercontent.com/u/583231){: style='height: 100px;' }](https://octodex.github.com/)


## Horizontal Rules

```markdown
***
```
***

```markdown
---
```
---


## Escaping

### Code
````markdown
```some-language
 ... some code ...
```
````


### Characters

To display a literal character that would otherwise be used to format text in a Markdown
document, add a backslash (`\`) in front of the character.

Character|Name|Character|Name
:-------:|----|:-------:|----
 \ | backslash  | { } | curly braces
 ` | backtick   | [ ] | brackets
 * | asterisk   | < > | angle brackets
 _ | underscore | ( ) | parentheses
 # | pound sign |  .  | dot
 + | plus sign  |  !  | exclamation mark
 - | minus sign |  \|  | pipe



