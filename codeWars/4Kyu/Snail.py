spi = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
spi2 = [
    [1,2,3,7,8],
    [4,5,6,9,9],
    [7,8,9,1,5],
    [3,5,6,3,4],
    [4,2,7,2,1]
]

def snail(snail_map):
    liSnail = []
    # print(snail_map[-1])
    while len(snail_map) > 0:
        # from left to right from top
        liSnail += snail_map[0]
        del snail_map[0]

        if(len(snail_map) > 0):
            # top to bottom right
            for i in snail_map:
                liSnail += [i[-1]]
                del i[-1]
            
            if snail_map[-1]:
                liSnail += snail_map[-1][::-1]
                del snail_map[-1]
            
            for i in reversed(snail_map):
                liSnail += [i[0]]
                del i[0]

    return liSnail



# snail(spi)
snail(spi2)