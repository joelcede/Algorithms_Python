import string

def abc():
    return string.ascii_letters

def find_missing_letter(chars):
    start, end = abc().index(chars[0]), abc().index(chars[-1])
    for i in range(start, end):
        if abc()[i] not in chars:
            return abc()[i]

print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(['O','Q','R','S']))