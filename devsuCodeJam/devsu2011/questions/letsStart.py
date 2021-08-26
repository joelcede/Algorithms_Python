# Create a function that receives two integers: x and y. 
# If any of them are 0 or negative, or if they are greater than 255, 
# the function should return -1

import random

li: int = [7,6,8,4,9,2,10,0,11,-2]

rest = 256 - len(li)
for _ in range(rest):
    li.append(random.randint(-10, 200))

def rangeIntegers(x: int, y: int) -> int:
    if x <= 0 or x > 255: return -1
    elif y <= 0 or y > 255: return -1
    else : return li[x-1] + li[y-1]

if __name__=="__main__":
    print(rangeIntegers(8, 50))
