def valid_parentheses(string):
    counter = 0
    listParentheses = [i for i in string if i == "(" or i == ")"]
    for i in listParentheses:
        if i == "(": counter += 1
        else: counter -= 1
        if counter == -1: break
    return False if(counter == -1 or counter >= 1) else True

print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))
print(valid_parentheses("hola(hi(xd)(df))"))