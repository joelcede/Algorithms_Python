# You are given an array with positive and negative integers. 
# Write a function to change the elements order in the array such that negative integers are at the beginning, 
# the positive integers are at the end. Zero (0) and integers that have the same sign don't change order
# For example, if the function receives: [4,-3,-100,7,0,1,-6] 
# the function should return: [-3, -100, -6, 4, 7, 0, 1]  
# The function receives an array of integers and return an array of integers.Limitations: 
# You CAN’T use sorting methods provided by the language. (eg. Array.sort(), sort(), etc...). 
# If you need to, you should create your own implementation of the sorting function.

a = [4,-3,-100,7,0,1,-6]

def orderLetRigth(li: list) -> list:
    #orderList, negativeList and positiveList
    orderedList, negativeList, positiveList = [], [], []
    for i in range(len(li)):
        if li[i] < 0:
            negativeList.append(li[i])
        else:
            positiveList.append(li[i])
    orderedList.extend(negativeList)
    orderedList.extend(positiveList)
    return orderedList

print(orderLetRigth(a))

#much text XD
