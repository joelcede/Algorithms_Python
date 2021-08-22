# Limitation:The conversion should be done considering the ASCII values. 
# Obviously you CAN’T use thefunctions provided by the language (toLowercase(), lowercase(), etc.). 
# You CAN’T have ahuge switch statement with cases for each letter, or lots of if/else statements.

a = "Ñañito, QUÉ bien! THIS is a sample text, Lorem Ipsum, 2 Be Converted."

def lowerCase(letters: str) -> str:
    return letters.casefold()

print(lowerCase(a))

# is ok?