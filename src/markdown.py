"""
Bla
"""
import src
import re
from .expressions import blockExp, inlineExp


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
                #print("Found a heading")
                mo = re.search(blockExp['Heading'], block)
                self._structure.append(self.converter.Heading(mo.group(3)))
            elif block.find('---')>=0 and block.find('---') <=3:
                #print("Found a horizontal line")
                pass
                #self._structure.append(self.converter)
            else:
                #print("Found a paragraph")
                self._structure.append(self.converter.Paragraph(block))
        return

    @property
    def structure(self):
        """
        Returns the converted text
        """
        return self._structure
