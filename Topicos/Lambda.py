# Lambda Function 
     # É uma função(pequena) sem nome
     # Pode ter vários argumentos mas somente 1 experessão
     # Muito utilizada dentro de outras funções
     # Código mais 'clean'

somar10 = lambda x, y: x + y + 10 

def somar(x):
    func2 = lambda x: x + 10 
    return func2(x)*4


def TopLambda(): 
    print(somar10(2, 4))
    #Dentro da própria função
    print(somar(10))