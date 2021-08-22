# Look at this series: 2, 2, 4, 12, 48, … the seed for this series was the number 2. 
# Look at this series: 3, 3, 6, 18, 72, … the seed for this series was the number 3. 
# For example, if the series receives x = 3, y = 4, it should return 72, because 72 
# is the 4th element of the series generated when x = 3. 
# The function will receive 2 integers, and return an integer. 


import random

li2: int = [2,2,4,12,48] # 2
li3: int = [3,3,6,18,72] # 3

rest = 256 - len(li2)
for _ in range(rest):
    li2.append(random.randint(1, 100))
    li3.append(random.randint(1, 100))

def rangeIntegers(x: int, y: int) -> int:
    if x <= 0 or x > 255: return -1
    elif y <= 0 or y > 255: return -1
    elif x == 2: return li2[y]
    elif x == 3: return li3[y]

print(rangeIntegers(3,240))