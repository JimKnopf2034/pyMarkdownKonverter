"""
Bla
"""
import src
import re

inlineExp = {"Bold":r"(\*{1,1})(\w+)(\1)",
            "italic": r"(\*{2,2})(\w+)(\1)",
            "italic bold": r"(\*{3,3})(\w+)(\1)"}
blockExp = {"Heading": r"(^ {0,3}#{1,4} ?)([0-9].*)?([A-Z].*)"}

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
        for block in self._input:
            if re.search(blockExp['Heading'], block) is not None:
                print("Found a heading")
                mo = re.search(blockExp['Heading'], block)
                self._structure.append(self.converter.Heading(mo.group(3)))
            elif line.find('---')>=0 and block.find('---') <=3:
                print("Found a horizontal line")
                #self._structure.append(self.converter)
            else:
                print("Found a paragraph")
                self._structure.append(self.converter.Paragraph(block))
        return
