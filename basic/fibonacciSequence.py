#Enter a number and have the program generate the Fibonacci sequence 
# to that number or to the Nth number.

li: list = [0, 1]
a: int = li[0]
b: int = li[1]

def isInt(num: int) -> int:
    while True:
        try:
            number = int(input(num))
            if number == -1: break
            else: return number
        except:
            print("Error, not is number!")

quantity: int = isInt("Number(-1 for leave): ")

for i in range(quantity-2):
    suma: int = a + b
    li.append(suma)
    a, b  = li[i+1], suma

print(li)
