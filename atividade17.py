#Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas
#(as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, 
#mostrando o resultado e saindo.

print("Escolha uma operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = int(input("Digite o número da operação desejada: "))

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if escolha == 1:
    resultado = valor1 + valor2
elif escolha == 2:
    resultado = valor1 - valor2
elif escolha == 3:
    resultado = valor1 * valor2
elif escolha == 4:
    if valor2 != 0:
        resultado = valor1 / valor2
    else:
        print("Divisão por zero não é permitida.")
else:
    print("Escolha inválida.")

print(f"Resultado: {resultado:.2f}")
