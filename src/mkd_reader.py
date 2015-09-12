import os

def read_markdown_file(path):
    if path is None:
        print("This is not a valid input file")
        return
    # check if path is a file
    if not os.path.isfile(path):
        print("This is not a valid input file")
        return
    input = []
    elem = ""
    with open(path) as datei:
        for line in datei.readline():
            if not line.strip() and elem.strip():
                input,append(elem)
            else:
                elem += line
    return input
