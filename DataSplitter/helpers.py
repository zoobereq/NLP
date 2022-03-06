def reader(filePath: str) -> list:
    listOfLines = []
    with open(filePath, 'r') as source:
        for line in source:
            line = line.rstrip()
            if line == False: # This condition takes care of empty lines.
                continue
            else:
                listOfLines.append(line)
    return listOfLines

def writer(filePath: str, source: list) -> None:
    with open(filePath, 'w') as sink:
        for line in source:
            print(line, file = sink)