# Let numbers be an array of integers.
# Get the maximum element in the array that produces the smallest sum when adding all the elements 
# that are different from itself.

numbers =  [1,2,3,3,3,3,4,5,6,6]

def mewms(number: list) -> int:
    li1, li2 = [], []
    setLi = list(set(number))
    for i in setLi:
        count = number.count(i)
        for _ in range(count): number.remove(i)
        li1.append(sum(number))
        for _ in range(count): number.insert(0,i)
        w = min(li1)
    for n in range(len(li1)):
        if li1[n] == w:
            li2.append(n) 
    return setLi[max(li2)]

if __name__=="__main__":
    print(mewms(numbers))