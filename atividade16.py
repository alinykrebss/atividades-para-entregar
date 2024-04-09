#Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: � =(𝑏𝑎𝑠𝑒�+𝑏𝑎�𝑒𝑛∗𝑎𝑙𝑡 2
#, lembre-se que a base maior e a base menor devem ser 
#números maiores que zero.

base_maior = float(input("Digite o valor da base maior: "))
base_menor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura: "))

area_trapezio = (base_maior + base_menor) * altura / 2

if base_maior > 0 and base_menor > 0:
    print(f"A área do trapézio é: {area_trapezio:.2f}")
    
else:
    print("Valores inválidos para as bases.")
