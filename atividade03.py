#Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o número ao quadrado.
import math

num1 = float(input(" digite um numero  "))

if num1 > 0 :
  raiz = math.sqrt(num1)
  print ( raiz)

else: num1 < 0
num2 = num1 ** 2  
print(num2)
