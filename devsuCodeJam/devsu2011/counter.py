# Given an array of integers, find which is repeated more times. 
# Return the number that has more repetitions. If two numbers has the same amount of repetitions, 
# return the lower number. 
# The most repeated number is 5. The function should return: 5. 
# Because 5 is repeated 3 times in the array)

A = [1, 5, 3, -2, 4, 2, 4, -2, 5, 5, 2, 1, 3]

def maxRepeat(lis: int) -> int:
    liSet: int = list(set(lis))
    counterIndex: int = []
    numbersEquals: int = []

    """count elements repeats in lis"""
    for i in range(len(liSet)):
        if liSet[i] in lis:
            counterIndex.append(lis.count(liSet[i]))

    maxNumber = max(counterIndex)
    count = -1

    """add to numbers equals the numbers repeats"""
    for j in counterIndex:
        if j == maxNumber:
            count += 1
            numbersEquals.append(count)
        else:
            count += 1

    """return position of liSet"""
    if len(numbersEquals) > 1:
        return liSet[min(numbersEquals)]
    else:
        return liSet[max(numbersEquals)]


print(maxRepeat(A))
