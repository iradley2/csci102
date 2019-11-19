def LoadFile(string):
    contents = open(string)
    contents = contents.read()
    contents.split("\n")
    return contents
