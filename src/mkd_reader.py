import os
import re

def read_markdown_file(path):
    """
    read_markdown_file
    ==================

    Only reads the text from the file and creates blocks of text. Blocks are distiguished from each other by blank lines.
    Every block is represented by a string. Blocks need to be splitted further down the process into lines.

    Creates a dictionary of configuration commands. Configuration commands can be things like the template to use, or
    author name , email, what ever

    Returns a list of blocks and a dictionary containing the configuration
    """

    if path is None:
        print("This is not a valid input file")
        return
    # check if path is a file
    if not os.path.isfile(path):
        print("This is not a valid input file")
        return
    input = []
    config = {}
    elem = ""
    with open(path, 'r') as datei:
        for line in datei.readlines():
            #extract config lines
            mo = re.match(r"(%#)([A-Z].*)(:)(.*)",line)
            if mo is not None:
                config[mo.group(2).lower()] = mo.group(4)
                continue
            # exract blocks
            if line.strip() == '' and not elem.strip() == '':
                input.append(elem)
                elem = ''
            elif line.strip()=='' and elem.strip() == '':
                # skip initial blank lines
                elem = ""
            else:
                elem += line
        input.append(elem)

    return (input, config)
