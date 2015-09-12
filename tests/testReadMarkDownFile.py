import unittest
import sys
import os

cwd = os.path.dirname(os.getcwd())
sys.path.append(cwd)

from src import read_markdown_file

class TestReadMarkdown(unittest.TestCase):
    def setUp(self):
        self.md_path = os.getcwd() + '/testdata/first_try.md'

    def testReadMarkdowFile(self):
        datei = read_markdown_file(self.md_path)
        return

if __name__ == '__main__':
    unittest.main()
