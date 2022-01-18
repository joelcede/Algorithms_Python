import string

def abc(index):
    return string.ascii_lowercase.index(index) + 1

# hacer una lista de string de x
# recorrer la lista de string separadas
# sumar y poner el resultado en otra lista
# comparar el listado 1 y el 2
def high(x):
    points = []
    for i in x:
        if i == abc(x):
            points.append(i)
    print(points)

print(high("man i need a taxi up to ubud"))