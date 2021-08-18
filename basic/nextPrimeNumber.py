#Have the program find prime numbers until 
#the user chooses to stop asking for the next one.

count: int = 0

while True:
    if count%2==1:
        print(count)
        count = count + 1
        nextQ: str = input("Next?[Y/N]: ")
        if nextQ == "Y".lower(): continue
        else: break
    else: count = count + 1