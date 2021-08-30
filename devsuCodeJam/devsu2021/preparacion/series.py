# Otherwise, the function should return the sum of thex and y elements of the series 
# The function will receive 2 integers, return an integer

def sumIndex(x: int,y: int) ->int:
    li: int = [7,6]
    if x <= 0 or x >= 255: return -1
    elif y <= 0 or y >= 255: return -1
    else:
        for i in range(255):
            if i%2==0: li.append(li[i]+1)  #sum +1 a numbers couple
            else:      li.append(li[i]-2)  #subtraction -2 a numbers impars
        return li[x-1] + li[y-1]

print(sumIndex(8,9))