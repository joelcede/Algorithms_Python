# Create a function that transform a string into a number. The number can be between 0 and 255. 
# The function will receive a string and return an integer


unid = ["zero","one","two","three","four","five","six","seven","eigth","nine"]
dec1 = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
dec2 = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
cent = ["one hundred","two hundred"]

def letter(word: str) -> int:
    n, w = 0, word.split()
    for i in range(len(cent)): 
        if cent[i] in word: n = n + (i+1) * 100
    for j in range(len(dec2)):
        if dec2[j] in word: n = n + (j+2) * 10
    for k in range(len(unid)):
        if unid[k] ==  w[-1]: n = n + (k * 1)
    for x in range(len(dec1)):
        if dec1[x] == w[-1]: n = n + (x+10)
    return n

print(letter("two hundred fifty six".lower()))

#not solves the return -1 :C