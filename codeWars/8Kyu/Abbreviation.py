def abbrev_name(name):
    nameSplit = name.title().split(" ")
    return ".".join([nameSplit[i][0] for i in range(len(nameSplit))])

print(abbrev_name("joel steven cedeño asuncion"))