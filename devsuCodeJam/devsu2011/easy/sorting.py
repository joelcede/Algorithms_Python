# Create a function that sorts an array of words in alphabetical order. 
# The text will always be lowercase, and won’t contain any special character or number. 
# Do not use sorting functions provided by the language (read the limitations)  
# Limitations: We want to make it interesting. Do not use any sorting function (sort, Array.sort(), etc.) 
# provided by the language. You can create your own sorting function.

import string

A = ["test", "contest", "programming", "more"]

def letters():
    return list(string.ascii_lowercase)

abc = letters()

def sortingLetters(lis: list) -> list:
    li = []
    for i in range(len(abc)):
        for j in range(len(A)):
            if A[j][0] == abc[i]:
                li.append(A[j])
    return li

print(sortingLetters(A))