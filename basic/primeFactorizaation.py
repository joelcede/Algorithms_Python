#Have the user enter a number and find all Prime Factors 
#(if there are any) and display them.

li: list = []
count: int = 2
number: int = int(input("Number: "))

while True:
    if number%count==0:
        number = number / count
        li.append(count)
    elif number <= 1: break
    else: count = count + 1

print("Prime Factors:",li)
print("Prime Factors without repeating:",set(li))