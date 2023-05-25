# Tuple -> Não adiciona itens

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo','verde','azul', 'vermelho')

from Topicos.Functions import *

def TopTuple():
    #Tuple -> Não se adiciona nem remove itens
        aula("Tuplas")
        print(type(cores_list))
        print(type(cores_tuple))

        duas_listas = cores_tuple*2
        print(duas_listas)

        cores_list.append('Roxo')
        print(cores_list)

        #Usar lista quando os itens for variáveis e Tuple quando a lista for fixa. -> Tuple gasta menos memória que list <-.
