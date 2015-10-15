import jinja2
import os

home = os.path.expanduser("~")

class LaTeXWriter():
    def __init__(self, parent):
        self.parent = parent
        self.loader = jinja2.FileSystemLoader(parent.template_dir)
        self.jenv = jinja2.Environment(loader=self.loader, trim_blocks=True, lstrip_blocks=True)
        self.template = None
        self.__tmp_path = None
        return

    def _create_temp_env(self):
        if os.path.exists(home+"/TMP_Dokumente/mdown"):
            self.__tmp_path = home+"/TMP_Dokumente/mdown"
            return
        self.__tmp_path = os.mkdir(home+"/TMP_Dokumente/mdown")
        return

    def write_to_template(self, markdown, template=None):
        if template is None:
            template = "latex_memo.j2"
        if self.template is None:
            self.template = self.jenv.get_template(template)
        if self.__tmp_path is None:
            self._create_temp_env()

        with open(self.__tmp_path+self.parent.outfilename, 'w') as out_file:
            out_file.write(self.template.render(data=markdown))
        return
