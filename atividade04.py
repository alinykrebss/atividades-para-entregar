#Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:a. O número digitado ao quadrado b. A raiz quadrada do número digitado
import math

num1 = float(input(" digite um numero  "))

if num1 < 0:
  print("numero invalido")

elif num1 > 0 :
  raiz = math.sqrt(num1)
  print ( raiz)

else : num1 > 0
num1 = num1 ** 2  
print(num1)
