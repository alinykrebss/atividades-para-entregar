#Leia um número fornecido pelo usuário. Se esse numero for positivo, calcule a raiz quadrada do número. 
#Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
import math

num1 = float(input(" digite um numero  "))

if num1 > 0 :
  raiz = math.sqrt(num1)
  print ( raiz)

else:
  print("seu numero eh invalido")
