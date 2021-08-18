#Just like the previous problem, but with e instead of PI. 
#Enter a number and have the program generate e up to that many decimal places. 
#Keep a limit to how far the program will go.

import random

while True:
    try:
        digit = int(input("Number(-1 for leave): "))
        if digit > 0 and digit < 48:
            print("{:.{}f}".format(random.uniform(digit,digit+1), digit))
        elif (digit == -1):
            break
        else:
            print("Limit exceeded!")
    except:
        print("Error, not is number!")
