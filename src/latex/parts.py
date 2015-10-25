from abc import ABCMeta, abstractmethod
from src import inlineExp, blockExp
import re

latex_inline_replace = {'Bold': r"\\textbf{%s}",
                        'Italic':r"\\textit{%s}",
                        'Italic bold':r"\\textit\\textbf{%s}"}

class AbstractPart(metaclass=ABCMeta):
    """docstring for AbstractPart"""
    def __init__(self, text):
        super(AbstractPart, self).__init__()
        self.text = text

    @abstractmethod
    def run_to_output(self):
        return

class List(AbstractPart):
    """
    List
    ====

    Information
    -----------

    Representation of a List created from markdown
    """
    def __init__(self, text):
        super().__init__(text)
        self.text = text
        self.output = []
        return

    def _create_open_string(self):
        self.output.append(r"\begin{itemize}")
        return

    def _create_close_string(self):
        self.output.append('\end{itemize}')
        return

    def _process_list(self):
        lines = self.text.split('\n')
        self._create_open_string()
        for elem in lines:
            print(elem, blockExp['List'])
            mo = re.match(blockExp['List'], elem)
            if mo is not None:
                self.output.append("\item %s" %mo.group(3))
        self._create_close_string()
        return

    def run_to_output(self):
        self._process_list()
        return "\n".join(self.output)

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


class Paragraph(AbstractPart):
    """
    Paragraph
    =========

    Information
    -----------

    A Paragraph is a textelement that can contain various other text elements, like links, inline code or decorations.
    The text is processed on element creation and returned as a single string. If inline elements are found they are
    included with LaTeX code in line.
    """
    def __init__(self, textelement):
        super(Paragraph, self).__init__(textelement)
        self.text = textelement
        self.__processed = False
        self._find_containing_markdown()

    def _find_containing_markdown(self):
        if self.__processed:
            raise ValueError
            return
        text = self.text.split('\n')
        for elem in text:
            for expr in inlineExp:
                mo = re.search(inlineExp[expr], elem)
                if mo is not None:
                    insert = latex_inline_replace[expr]%mo.group(2)
                    text[text.index(elem)] = re.sub(inlineExp[expr],insert, elem)
        self.text = '\n'.join(text)
        return

    def run_to_output(self):

        return self.text


class HorizontalLine(object):
    """
    HorizontalLine
    ==============

    Information
    -----------

    Inserts a horizontal line into the text, not sure if this is supported in LaTeX
    """
    def __init__(self, text):
        super(HorizontalLine, self).__init__()
        self.text = text

    def run_to_output(self):
        return
