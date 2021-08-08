"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
"""

def namelist(names):
    x, l = "", len(names)
    for i in range(l):
        x += names[i]['name']
        if i == l - 2: x += " & "
        elif i == l - 1: x += ""
        else: x += ", "
    return x