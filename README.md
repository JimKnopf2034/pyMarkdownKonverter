# pyMarkdownKonverter

This is the idea of a converter from Markdown to LaTex, but also possible to other formats in future. The idea is to read in the markdown and than create a list of objects that represent the elements possible in Markdown. The Elements all share a common interface, due to which they can be rendered to a template.

As the template language jinja2 is planed.

# Markdown conventions

1. Assume all elements are ordered in blocks which are divided by blank lines
2. Code is assumed to be fenced in three backticks
3. Headers are only in ATX-Version allowed for the beginning
