# Create a function that receives a 32 bit integer and return the number of ones in the binary of that number. 
# (caution: looping through testing each bit is not a solution). 
# For example: If the function receives 25, it should return 3. 
# Why? Because 25 in binary is 11001, which has 3 ones

def countOneBits(number: int) -> int:
    conv, li = bin(number)[2:], []
    for i in range(len(conv)): li.append(int(conv[i]))
    return li.count(1)

if __name__=="__main__":
    print(countOneBits(25))
