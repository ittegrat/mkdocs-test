# Extended Syntax

## Tables

| Syntax | Description | Test Text |
| :---   |    :---:    |      ---: |
| Header    | Title | A very long title |
| Paragraph | Text  | And more          |


## Fenced Code Blocks

~~~markdown
```json
{
  "firstName": "John",
  "lastName": "Smith",
}
```
~~~

```json
{
  "firstName": "John",
  "lastName": "Smith",
}
```


## Footnotes

```markdown
Here's a simple footnote[^1], and here's a longer one[^bignote].

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.

///Footnotes Go Here///
```

Here's a simple footnote[^1], and here's a longer one[^bignote].

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.

///Footnotes Go Here///


## Definition Lists

```markdown
First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.
```
First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.


## Admonition

```markdown
!!! type "optional explicit title within double quotes"
    Any number of other indented markdown elements.

    This is the second paragraph.
```

!!! tip
    You should note that the title will be automatically capitalized.

!!! hint
    You should note that the title will be automatically capitalized.

!!! important
    You should note that the title will be automatically capitalized.

!!! note
    You should note that the title will be automatically capitalized.

!!! warning
    You should note that the title will be automatically capitalized.

!!! caution
    You should note that the title will be automatically capitalized.

!!! attention
    You should note that the title will be automatically capitalized.

!!! error
    You should note that the title will be automatically capitalized.

!!! danger
    You should note that the title will be automatically capitalized.

!!! type_not_styled
    A type not styled is rendered like a 'note' admonition .

!!! danger "Don't try this at home"
    This is an admonition with an explicit title.

!!! important ""
    This is an admonition box without a title.
