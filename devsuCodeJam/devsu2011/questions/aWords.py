# If the function receives: “this is a sample text, it has a lot of analysis.” 
# The function should return 5, since five words has “a” characters. (a, sample, has, a, analysis). 
# Limitations: Do not use the split() function, or similar.

a = "this is a sample text, it has a lot of analysis."

def splitWords(letters: str) -> str:
    letter: str = []
    word: str = ""
    for i in letters:
        if i != " ": word = word + i
        else: 
            letter.append(word)
            word = ""
    letter.append(word)
    return letter

def countWords(word: str) -> int:
    words = splitWords(word) 
    count = 0
    for i in range(len(words)):
        if "a" in words[i]:
            count+=1
    return count   

if __name__=="__main__":
    #print(splitWords(a))
    print(countWords(a))

#It's hard whithout .split()?