# Set (Listas)
    # Similar a listas
    # Evita itens duplicados 
    # Não utiliza index

num1 = {1,2,3,4,5,6}
num2 = {4,5,6,7,8,9}

listSet1 = set([1,2,3,4,5,6])
s1 = {1,2,3,4,5,6}

set2 = {'a','b','c'}
set3 = {'a','b','e'}
set4 = {'a','b','f'}

from Topicos.Functions import *



def TopSet():
    # Sets 
      # 1. Perde o index
      # 2. Evita números duplicados
      
      aula("Sets")

      print(num1,num2)
      print(num1|num2) # Union
      print(num1-num2) # Difference
      print(num1 ^ num2) # Symmetric Difference (Retira as insterceções)
      print(num1 & num2) # And (Apenas a interceção)

      s1.add(7)
      s1.add(4)
      s1.update([6,7,8,9,10])
      s1.remove(10)
      s1.discard(90)

      print(listSet1)
      print(s1)
      print(type(listSet1))
      print(type(s1))

      set5 = set2.symmetric_difference(set3)
      print(set5)
      set5 = set3.difference(set3)
      print(set5)