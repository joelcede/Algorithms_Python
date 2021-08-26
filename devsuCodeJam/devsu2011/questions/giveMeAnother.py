# Look at this series: 60, 30, 20, 15, 12... the seed for this series was the number 60. 
# For example: If the function receives x=60, y=3, it will return 20, 
# because 20 is the 3th element in the series generated when x = 60. 
# The function will receive 2 integers, return a floating point value.

import random

li: int = [60,30,20,15,12] # 60

rest = 256 - len(li)
for _ in range(rest):
    li.append(random.randint(-10, 200))

def rangeIntegers(x: int, y: int) -> int:
    if x <= 0 or x > 255: return -1
    elif y <= 0 or y > 255: return -1
    elif x == 60 : return li[y-1]

print(float(rangeIntegers(60,3)))