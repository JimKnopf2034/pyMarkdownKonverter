import jinja2
import os

home = os.path.expanduser("~")

class LaTeXWriter():
    def __init__(self, parent, config=None):
        self.parent = parent
        self.loader = None
        self.jenv = None
        self._config = config
        self.template = None
        self.__tmp_path = None
        return

    def __create_environment(self, tpath):
        self.loader = jinja2.FileSystemLoader(tpath)
        self.jenv = jinja2.Environment(loader=self.loader, trim_blocks=True, lstrip_blocks=True)
        return

    def _create_temp_env(self):
        if os.path.exists(home+"/TMP_Dokumente/mdown"):
            self.__tmp_path = home+"/TMP_Dokumente/mdown"
            return
        self.__tmp_path = os.mkdir(home+"/TMP_Dokumente/mdown")
        return

    def write_to_template(self, markdown, template=None):
        #:TODO: needs rework!
        def get_template_path():
            for folder in self.parent.template_dir:
                for file in os.listdir(folder):
                    if file == template:
                        return (os.path.abspath(folder), file)

        if not self._config is None:
            if 'template' in self._config.keys():
                template = self._config['template']

        if template is None:
            template = "./latex_memo.j2"
            self.__create_environment(os.getcwd())
        else:
            if not os.path.isfile(template):
                tpath, template = get_template_path()
                self.__create_environment(tpath)

        if self.template is None:
            self.template = self.jenv.get_template(template)
        if self.__tmp_path is None:
            self._create_temp_env()

        with open(self.__tmp_path+'/'+self.parent.outfilename, 'w') as out_file:
            out_file.write(self.template.render(data=markdown))
        return
