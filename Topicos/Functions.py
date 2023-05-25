# Functions (Funções)
   # DRY - Don't repeat yourself
   # Vários Argumentos (xargs) indentificando o Parametro

#Funções para vários argumentos

def soma(*numeros):
    resultado = 0 
    for num in numeros:
        resultado += num
    return resultado

# Criar uma função que armazena numeros e strings 
# * - Variável comum 
# ** - List

def agencia(**carro):
    return carro 

#Função para infomar aula
def aula(x):
    print("")
    print("Aula de {}".format(x))
    print("")

def TopFunctions():
    aula("Funções")
    x = soma(1,2,3,4,10,20)
    print(x)
    print(agencia(marca = 'Gol',cor = 'Branca', motor = 1.0, placa = 1234))