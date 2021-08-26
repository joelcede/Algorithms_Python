# Look at this series: 3, 6, 24, 144, … the seed for this series was the number 3 
# For example, if the function receives x = 3, y = 1, z = 3, 
# the function will find (based on x), that the series is 3, 6, 24, 144, …, 
# based on that series, and based on y=1 and z=3, the function should return 33.

def series2(x: int,  y: int, z: int) -> int:
    serie, init, end, count = [], y, z, 0
    serie.append(x)
    if x <= 0 or x > 255: return -1
    elif y <= 0 or y > 255: return -1
    elif z <= 0 or y > 255: return -1
    else:
        for i in range(255):
            count += 2
            serie.append(serie[i]*count)
        return sum(serie[init-1:end])

print(series2(5,2,2))
