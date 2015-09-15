from abc import ABCMeta, abstractmethod

class AbstractPart(metaclass=ABCMeta):
    """docstring for AbstractPart"""
    def __init__(self, text):
        super(AbstractPart, self).__init__()
        self.text = text

    @abstractmethod
    def run_to_output(self):
        return


class Heading(AbstractPart):
    """
    Heading
    =======

    Information
    -----------

    Representation of a Heading created from markdown. Goes until 4th level in Latex. Returns the String with section or
    subsection or subsubsection. If Level is deeper than subsubsection, a paragraph is returned. Subparagraphs are not
    available.
    Heading level is retrieved from the number of #-symbols at the beginng of the element

    An Element is only interpreted as a heading, if the line starts with #-symbols. Trailing #-symbols are ignored.
    """
    def __init__(self, text):
        super(Heading, self).__init__(text)
        self.text = text
        self.output = None
        self.prefix = None
        self.level = 0

    def _get_level(self):
        text = self.text.strip().split()
        for char in text[0]:
            if char == '#':
                self.level += 1
        #print(self.level)
        self.prefix = "sub" * (self.level-1)

    def _extract_content(self):
        self.output = self.text.replace("#","").strip()
        return

    def run_to_output(self):
        self._get_level()
        self._extract_content()
        if self.level > 3:
            return "\paragraph{%s}"%self.output
        return "\%ssection{%s}"%(self.prefix,self.output)


class Paragraph(object):
    """
    Paragraph
    =========

    Information
    -----------

    A Paragraph is a textelement that can contain various other text elements, like links, inline code or decorations.
    """
    def __init__(self, arg):
        super(Paragraph, self).__init__()
        self.arg = arg

    def _find_containing_markdown(self):
        return

    def run_to_output(self):
        return
