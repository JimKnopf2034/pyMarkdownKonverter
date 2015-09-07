"""
Bla
"""

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
        self._structure = []
        return

    @classmethod
    def toLaTex(cls, markdown, template=None):
        obj = MarkDown(markdown, "LaTeX")
        return

    def parse_text(self):
        for line in self._input:
            if line.find('#') >0:
                print("Found a heading")
                self._structure.append(Heading(line))
        return
