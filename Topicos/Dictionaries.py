# Dictionaries (Dicionários)
       # Utilizad index no formato de Keys e Values 
       # Aceita string, integer, float, bloolean...
      
from Topicos.Functions import *

aluno = {
  'nome':'Ana',
  'idade':16,
  'nota_final':'A',
  'aprovação': True,
  'Materias': ['Fisica', 'Matemarica', 'Ingles']
}

def TopDictioneries():
    aula("Dicionários")
    
    print(aluno['nome'])
    print(aluno['idade'])
    
    # Update

    aluno.update({'endereco': 'Rua A'})

    print(aluno.get('endereco','Não existe')) #Não existe caso não tenha

    # Delete 
     
    del aluno['idade']

    print(aluno)
    

    # For Loop 

    for x in aluno: # Imprime apenas as Keys (Mesmo que aluno.keys())
        print(x) 
    
    print("")

    for x in aluno.values(): 
        print(x)

    print("")    

    for keys, values in aluno.items():
        print(keys, values)

    #Como organizar as listas

    print(aluno.get('Materias')) # Gets apenas em materias
    print("")
    print(len(aluno)) # Numeros de tuplas
    print("")
    print(aluno.items)
    print(aluno.keys())
    print(aluno.values()) 
