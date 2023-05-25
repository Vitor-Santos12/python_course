# Map Function 
    # Muito utilizado com listas
    # Aplicar uma função a um Iterable, por item. (list, tuple, dic etc.)

global lista1
global lista2
global lista3

lista1 = [1, 2, 3, 4]
valores = [10,12,34,44,57]

def multi(x):
    return x*2

lista2 = map(multi, lista1)

def TopMap():
    print("")
    print('Apenas Map')
    print("")
    print(list(lista2))

# Map com Lambda

lista3 = map(lambda x: x * 2, lista1)


def TopMapLambda():
    print("")
    print("Map com Lambda")
    print("")
    print(list(lista3))
    print("")
    print("Map com Lambda apenas no Print")
    print("") 
    print(list(map(lambda x: x * 4, lista1))) # Formato de lista

def remover20(x):
    return x > 20

def TopFilter():
    print("")
    print('Com função')
    print("")
    print(list(filter(remover20, valores)))
    print("")
    print('Apenas com Print')
    print("")
    print(list(filter(lambda x: x > 20, valores)))

    