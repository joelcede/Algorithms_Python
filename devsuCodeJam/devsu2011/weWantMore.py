# Given a string, which contains words and spaces (no special characters), 
# create a functionthat return a string with the words in a reverse order. 
# Example:
# If the function receives: “this is a test”, it should return: “test a is this”.

def reverseWords(b: str) -> str:
    li: str = b.split()
    li.reverse()
    return " ".join(li)

print(reverseWords("this is a test"))
