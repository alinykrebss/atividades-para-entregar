#Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem “Números iguais”.



num1 = float(input(" digite o primeiro numero "))
num2 = float(input(" digite o segundo numero "))

if num1 > num2:
    print(" o maior eh", num1)

elif num2 > num1:
    print( "o maior eh ", num2)

else:
    print(" os numeros sao iguais")