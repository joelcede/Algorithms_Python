import string

def abc(index):
    return string.ascii_lowercase.index(index) + 1

def high(x):
    points = []
    total = 0
    listX = x.split(" ")
    for item in range(len(listX)):
        longLetter = len(listX[item])
        for x in range(longLetter):
            total += abc(listX[item][x])
        points.append(total)
        total = 0
    return listX[points.index(max(points))]

print(high("man i need a taxi up to ubud"))
print(high("aa b"))