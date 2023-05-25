from sys import getsizeof

# Generetor Expressions
   # Uma forma mais rápida para Listas, dicionários e etc
   # Menos memória alocada
   # Valores em bytes

global numeros1



def GeneretorExpressions():
      numeros1 = [x*10 for x in range(1000000)]
      print(type(numeros1))
      #print(numeros1)
      print(getsizeof(numeros1))

      print('======')

      numeros1 = (x*10 for x in range(1000000))
      print(type(numeros1))
      #print(list(numeros1))
      print(getsizeof(numeros1))

