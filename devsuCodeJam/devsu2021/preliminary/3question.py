
# def search(index: int):
#     count, li = 0, []
#     for i in range(1,index):
#         count += 1
#         container: int = count
#         if i%4==0: count -= 2
#         li.append(container)
#     return li[index]

#print(search(46))

def search(index: int):
    count: int = 2
    for i in range(0,index+1):
        if i%4==0: count -=2
        count += 1
    print(count)
search(4611686018327187)


