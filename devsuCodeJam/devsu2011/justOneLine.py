# Write a function to remove duplicates from a sorted array of integers. 
# Pretty easy, right?What about making it in one line of code? 
# (You can use as many statements as needed, butthe code should be written in one line)

def removeDuplicates(a: int) -> list: return list(sorted(set(a)))

print(removeDuplicates([-3, -2, 0, 0, 5, 7, 9, 11, 11, 25]))