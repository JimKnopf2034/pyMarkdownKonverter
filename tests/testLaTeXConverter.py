from unittest import TestCase
from ..src.latex import *

class TestLaTeX(TestCase):
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
        return
