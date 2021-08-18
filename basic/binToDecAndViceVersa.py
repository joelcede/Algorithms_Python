#Develop a converter to convert a decimal number to binary or a binary number 
# to its decimal equivalent.


while True:
    a: str = input("covert to Binary or Decimal?[B/D]: ").lower()
    if a == "b":
        number: int = int(input("Number: "))
        print(bin(number)[2:])
    elif a == "d":
        number: int = int(input("Number: "))
        print(int(str(number), 2))
    else:
        break