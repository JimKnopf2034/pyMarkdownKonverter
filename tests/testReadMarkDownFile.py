import unittest
import sys
import os

cwd = os.path.dirname(os.getcwd())
sys.path.append(cwd)

from src import read_markdown_file
from src import MarkDown

class TestReadMarkdown(unittest.TestCase):
    def setUp(self):
        self.md_path = os.getcwd() + '/testdata/first_try.md'

    def testReadMarkdowFile(self):
        datei = read_markdown_file(self.md_path)
        return

    def testCorrectSplittingIntoBlocks(self):
        datei = read_markdown_file(self.md_path)
        self.assertEqual(len(datei), 4)
        return

    def testParseForHeadings(self):
        datei = read_markdown_file(self.md_path)
        md = MarkDown.toLaTex(datei)

        return

if __name__ == '__main__':
    unittest.main()
