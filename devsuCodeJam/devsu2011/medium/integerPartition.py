# Esquemas Ferrers
# https://ztfnews.wordpress.com/2014/08/11/los-diagramas-de-ferrers/

# In number theory, a ​partition​ of a positive integer ​n​, also called an ​integer partition​, 
# is away of writing ​n​ as a sum of positive integers. 
# Two sums that differ only in the order of theirsummands are considered to be the same partition.
# For example: If the function receives 4, it should return 5. If it receives 8, it will return 22, etc.

import math

def partitions(n: int) -> int:
    if n <= 0 or n > 255: return -1
    return int((math.exp(math.pi * math.sqrt(2*n/3))) / (4*n * round(math.sqrt(3))))

if __name__=="__main__":
    print(partitions(8))
