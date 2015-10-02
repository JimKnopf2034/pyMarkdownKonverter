#!/usr/bin/python3
"""MarkDownKonvert

Usage: convert_markdown.py <markdownFile> <outFileName>
       convert_markdown.py (-h | --help)

Options:
    -h --help   show this message

This is a converter from Markdown to Anything, starting with LaTeX as first target format. Other formats may be added later.
"""
from docopt import docopt
from src import read_markdown_file, MarkDown

class MarkDownKonvert(object):
    """docstring for MarkDownKonvert"""
    def __init__(self, args):
        super(MarkDownKonvert, self).__init__()
        self._input = args['<markdownFile>']
        self.outfilename = args['<outFileName>']


    def run(self):
        """
        Start the conversion process
        """
        print('Welcome to MarkdownKonvert, a converter from Markdown to LaTeX')
        md = MarkDown.toLaTex(read_markdown_file(self._input),None)
        return


if __name__ == '__main__':
    arguments = docopt(__doc__)
    #print(arguments)
    mdk = MarkDownKonvert(arguments)
    mdk.run()
