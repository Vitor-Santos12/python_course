# Listas 
         # Armazenar mais de uma informação em variáveis
         # Manter a sequencia dos dados em uma variável 

cidade1 = "Rio de Janeiro"
cidade2 = "São Paulo"
cidade3 = "Salvador"

cidades = ["Rio de Janeiro","São Paulo", "Salvador"]

itens = [['item1','item2'],['item3','item4']]

# Extraindo variáveis de listas
#Exercicio 01 
produtos = ['arroz','feijão','laranja','banana']
#              1       2         3         4
item1, item2, item3, item4 = produtos
#Exercicio 02
produtos1 = ['arroz','feijão','laranja','banana',5,6,7,8]
#              1       2         3         4
p1item1, p1item2, p1item3, *p1outros = produtos1
#Exercicio 03
produtos2 = ['arroz','feijão','laranja','banana',5,6,7,8]
#              1       2         3         4
p2item1, p2item2, *p2outros, p2item8 = produtos2

# Looping dentro de uma lista 

valores = [50, 80, 110, 150, 170]

cores = ['amarelo', 'verde', 'azul', 'vermelho']

# Agregando Duas Listas zip

valores1 = [10, 20, 30, 40]


from Topicos.Functions import *

def TopLista():
        
        aula("Lista")
        
        print("Aula de Funções!")
        print(cidades[0])

        cidades[0] = 'Brasilia'
        print(cidades[0])
        # Para adicionar na parte final da lista
        cidades.append("Santa Catarina")
        print(cidades)
        # Para remover na parte final da lista 
        cidades.remove("Salvador")
        print(cidades)
        # Insere em determinadas posições
        cidades.insert(1, "Fortaleza")
        #remover determinada inserção 
        cidades.pop()
        print(cidades)

        #Concatenando Lista 
        numeros = [2,3,4,5]
        letras  = ['a','b','c','d']
        final = numeros + letras
        print(final)

        print(itens[0][1])

        # Extraindo variáveis de Listas
        #Exercicio 01 
        print(item1)
        print(item2)
        print(item3)
        print(item4)
        #Exercicio 02
        print(p1item1)
        print(p1item2)
        print(p1item3)
        print(p1outros)
        #Exercicio 03
        print(p2item1)
        print(p2item2)
        print(p2outros)
        print(p2item8)

        # Looping dentro de uma lista

        for x in valores:
            print(f' O valor final do produto é de R${x}.')

        # Verificaçõa de cores

        # while(True):

        #       cor_cliente = input('Digite uma cor:') 

        #       if cor_cliente in cores:
        #           print('Em estoque!')
        #       else:
        #           print('Não temos essa cor em estoque!')
        #           break

        # Agregando Duas Listas com o Zip

        duas_listas = zip(cores,valores)
        tres_listas = zip(cores,valores,valores1)
        print(duas_listas)
        print(list(duas_listas))
        print(list(tres_listas))

        #Input em uma lista 

        # frutas_usuario = input('Digite o valor das frutas separados por virgulas: ')

        # frutas_lista = frutas_usuario.split(', ')

        # print(frutas_lista)