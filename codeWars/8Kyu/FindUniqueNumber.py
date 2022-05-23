""" There is an array with some numbers. All numbers are equal except for one. 
    Try to find it!
"""
"""    x = set([x for x in arr if arr.count(x) > 1])
    return list(set(arr).difference(x))[0]
    arr.count(arr[0]) """
from collections import Counter

def find_uniq(arr: list) -> int:
    counter = list(Counter(arr).values())
    return list(Counter(arr).keys())[counter.index(1)]


a = [ 1, 1, 1, 2, 1, 1, 2, 2, 4, 3, 3 ]
print(find_uniq(a))