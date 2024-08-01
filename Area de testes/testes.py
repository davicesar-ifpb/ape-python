lista = [1,2,1,3,1,4,5,1]

def implementacao1():
    lista2 = list(filter(lambda x : x != 1, lista))

    print(lista2)


def implementacao2():
    lista2 = lista.copy()
    for _ in range(lista2.count(1)):
        lista2.remove(1)

    print(lista2)


def implementacao3():
    lista2 = lista.copy()
    while 1 in lista2:
        lista2.remove(1)

    print(lista2)


implementacao1()
implementacao2()
implementacao3()