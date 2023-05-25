#Erros 
    # Excelente para teste 
    # Não realiza o 'stop' no probrama
    # Mensagens customizadas quando encontra um erro

def TopErros():
      
      try:
          letras = ['a','b','c']
          print(letras[3])
      except IndexError:
          print('Não existe! ')    


def TopErrosInput():
      
      try:
          valor = int(input('Digite o valor do seu produto: '))
          print(valor)
      except ValueError:
          print('Por favor insira um numero inteiro!')    

def TopErrosFinally():
      try:
          valor = int(input('Digite o valor do seu produto: '))
          print(valor)

      except ValueError:
          print('Por favor insira um numero inteiro!')

      finally: 
          print('código ok')


      # else:
      #     print('O usuário digitou o valor correto')
      #     resultado = valor * 2 
      #     print(resultado)

      
              