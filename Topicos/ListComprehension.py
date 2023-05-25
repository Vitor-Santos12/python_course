# List Comprehension 
       # Mais simples de se escrever 
       # Utilizando quando você precisa criar uma nova lista a partir de uma existente
       # [expressao for iten in itens]

global frutas1
global frutas2
global valores 
global valores1

frutas1 = ['abacate', 'banana', 'morando', 'kiwi', 'abacaxi']
frutas2 = []
valores1 = []
valores2 = []

def ListComprehension():
    for iten in frutas1:
        if 'b' in iten:
          frutas2.append(iten)
    print("")
    print('ListComprehension')
    print("")
    print(frutas2)
    print("")
    print('ListComprehension em uma linha')
    print("")
    frutas3 = [iten for iten in frutas1 if 'n' in iten]
    print(frutas3)
    print("")
    print('ListComprehension em uma linha com intenger')
    print("")
    for x in range(6):
          valores1.append(x * 10)

    print("")
    print(valores1)
    print("")
    print('ListComprehension em uma linha com intenger em uma linha')
    print("")
    valores2 = [x * 10 for x in range(6)]
    print(valores2)