"""
This is a converter from Markdown to Anything, starting with LaTeX as first target format
"""

class MarkDownKonvert(object):
    """docstring for MarkDownKonvert"""
    def __init__(self, input, output=None):
        super(MarkDownKonvert, self).__init__()
        self._input = input

    def run(self):
        """
        Start the conversion process
        """
        return


if __name__ == '__main__':
    print("Welcome to Markdown Konverter")
    mdk = MarkDownKonvert()
    mdk.run()
