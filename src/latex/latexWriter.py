import jinja2
import os

class LaTeXWriter():
    def __init__(self, parent):
        self.parent = parent
        self.loader = jinja2.FileSystemLoader(parent.template_dir)
        self.jenv = jinja2.Environment(loader=self.loader, trim_block=True, lstrip_blocks=True)
        self.template = None
        return

    def write_to_template(self, markdown, template):
        if self.template is None:
            self.template = jenv.get_template(template)

        with open(self.parent.outfilename, 'w') as out_file:
            out_file.write(self.template.render(data=markdown))
        return
