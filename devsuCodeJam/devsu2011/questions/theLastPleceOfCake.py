# Equilibrium index of a sequence is an index such that the sum of elements at lower indexes is equal 
# to the sum of elements at higher indexes. 
# For example, if the array received is: A=[-7, 1, 5, 2, -4, 3, 0] 3 is an equilibrium index, 
# because:A[0]+A[1]+A[2] = A[4]+A[5]+A[6] In other words, 
# you should find the index of the array where the sum of the left elements is equal to the sum 
# of the right elements. In the example, the function will return 3, 
# because it’s the first equilibrium index found in the array.

A = [- 7, 1, 5, 2, -4, 3, 0]

def equilibrium(li: int) -> int:
    counted, invertCount, sum1, sum2 = 0, -1, 0, 0

    for i in range(len(li)):
        sum1 += li[i]
        sum2 += li[invertCount]
        invertCount -= 1
        if sum1 == sum2:
            counted += 1
            break
        elif sum1 != sum2: counted += 1
        else: return -1
    return counted

print(equilibrium(A))
