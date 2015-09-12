import unittest
import sys
import os

cwd = os.path.dirname(os.getcwd())
sys.path.append(cwd)

from src.latex import *

class TestLaTeX(unittest.TestCase):
    """
    TestLaTeX
    =========

    Information
    -----------

    Testcase for Latex render objects. Test every object once. Possible objects are:

    - Heading
    - Paragraph

    """

    def testHeading(self):
        hd = Heading("# Das ist ein Titel #")
        print(hd.run_to_output())
        hd = Heading("## Das ist ein untertile")
        print(hd.run_to_output())
        return


if __name__ == '__main__':
    unittest.main()
