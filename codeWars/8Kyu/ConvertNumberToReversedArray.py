""" Conver number to reversed array of digits
"""

def digitize(n):
    if isinstance(n, int): return [int(i) for i in reversed(str(n))]


n = 35231
print(digitize(n))