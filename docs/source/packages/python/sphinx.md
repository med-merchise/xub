# Sphinx

## Install Sphinx

We install Sphinx locally in a Python project using [](#uv):

```
uv add --group docs sphinx myst-parser
```

[MyST-Parser] is a Sphinx and Docutils extension to parse MyST, a rich and
extensible flavour of [Markdown], known as [CommonMark], for authoring
technical and scientific documentation.

To configure this extension, in your Sphinx configuration file (`conf.py`):

```python
extensions = [
    'myst_parser',
    ...
```

To enable some syntax Extensions set the [`myst_enable_extensions`][mystx]
variable:

```python
myst_enable_extensions = [
    'attrs_block',
    'attrs_inline',
    ...
]
```

## Some MyST Markdown References

- [How to link to URLs, documents, headings, figures, ...][myst-cr].
- [Using roles and directives][myst-rd] with the same capabilities as in
  `reStructuredText`.
- [How to organise your content into multiple documents][org-cont]

[markdown]: https://www.markdownguide.org/
[commonmark]: https://spec.commonmark.org/
[myst-parser]: https://myst-parser.readthedocs.io/
[mystx]: https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
[org-cont]: https://myst-parser.readthedocs.io/en/latest/syntax/organising_content.html
[myst-cr]: https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html
[myst-rd]: https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html
