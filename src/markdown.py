"""
Bla
"""
import src

class MarkDown():
    """
    MarkDown
    ========

    Information
    -----------

    Basic class to convert from markdown to latex or what ever. Gets  an input text and converts this, via konverter functions
    """
    def __init__(self, markdown, target):
        self._input = markdown
        self._target = target
        self._structure = []
        self.__load_converter_module()
        return

    def __load_converter_module(self):
        if self._target == 'LaTeX':
            self.converter = src.latex
        return

    @classmethod
    def toLaTex(cls, markdown, template=None):
        obj = MarkDown(markdown, "LaTeX")
        obj.parse_text()
        return obj

    def parse_text(self):
        for line in self._input:
            print(line)
            if line.stript().find('#') =0:
                print("Found a heading")
                self._structure.append(self.converter.Heading(line))
            elif line.find('---')>=0 and line.find('---') <=3:
                print("Found a horizontal line")
                self._structure.append(self.converter)
        return
