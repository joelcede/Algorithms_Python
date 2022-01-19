p1 = 'abba'
p2 = 'abbbaz'
p3 = 'bbaa'

"""se = list(set(p1))
print(p2.count(se[1]))
print(p1.count(se[1]))"""

def anagrams(word, words):
    setter1 = list(set(word))
    setter2 = list(set(words))
    for i in setter2:
        if i not in word: 
            print("Hola")
            return False
        return True
anagrams(p1,p2)
