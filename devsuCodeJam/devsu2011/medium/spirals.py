# Given a  2-D matrix of characters, write a function that returns a string with the 
# charactersfrom the matrix in spiral order. (Starting from [0][0] element, next element: [0][1], etc... ).
# The matrix can have any length, but it will always be a square.
# Return a string with the value: “abcfihgde”.
# me this algorithm is very bad XD.

f = [
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"],
]

def spiralBad(array2D: list) -> str:
    a, b, c, u, x = "", "", "", [], 0
    for i in range(len(f)):
        for j in range(len(f[i])):
            x = len(f[i])
            u.append(f[i][j])
    for i in range(x-1): a+=u[i]
    for j in range(x-1,len(u),x): a+=u[j]
    for k in range((len(u)-x), len(u)-1): b+=u[k]
    a += b[::-1]
    for l in range(x, len(u)-x,x): c+=u[l]
    a += c[::-1]
    return a+array2D[1][1]

print(spiralBad(f))