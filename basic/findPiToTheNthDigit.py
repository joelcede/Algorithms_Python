#Enter a number and have the program generate PI up to that many decimal places. 
#Keep a limit to how far the program will go.
import math

while True:
    try:
        digit = int(input("Number(-1 for leave): "))
        print("{:.{}f}".format(math.pi,digit) if digit>0 and digit<48 else "Limit exceeded!" )

    except:
        print("Error, not is number!")
