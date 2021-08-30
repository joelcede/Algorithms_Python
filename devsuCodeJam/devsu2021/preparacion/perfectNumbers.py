# A perfect number is a positive integer that is equal to the sum of its proper divisors. 
# Create a function that receives two values X and Y and return the smaller perfect number found, 
# which is greater or equal than X and lower or equal than Y. 
# If no perfect number found, it should return -1 
# For example, if the function receives X=5, Y=7, 
# it should return 6, because 6 is the smaller perfect number between 5 and 7

def perfectN(x: int, y: int) -> int:
    listReal: int = []
    numberReal: int = 0
    for RealNumber in range(x+1, y+1):
        while True:
            """subs the number and the round"""
            RealNumber = round(RealNumber / 2)
            if RealNumber <= 1: break
            else: 
                RealNumber+=RealNumber
                numberReal = RealNumber
                break
        if RealNumber == numberReal:
            """add to the list the numbers reals"""
            listReal.append(numberReal)
        elif listReal == []:
            return -1
    """remove the elements repeated and shearh min of the list"""
    return min(list(set(listReal)))


print(perfectN(5,7))

# copied and pasted of algorithm perfect number of the devsu2011, bad englis :c.