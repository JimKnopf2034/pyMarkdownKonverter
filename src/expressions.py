inlineExp = {"Bold":r"(\*{1,1})(\w+)(\1)",
            "Italic": r"(\*{2,2})(\w+)(\1)",
            "Italic bold": r"(\*{3,3})(\w+)(\1)"}
blockExp = {"Heading": r"(^ {0,3}#{1,4} ?)([0-9].*)?([A-Z].*)",
            "List": r"(^ {0,3}(-|\*) ?)([a-zA-Z0-9].*)"}
