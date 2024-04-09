#Ler um número inteiro. Se o número lido for negativo, escreva a mensagem “Número inválido”.
# Se o numero for positivo, calcular o logaritmo deste número.

import math

try:
    numero = int(input("Digite um número inteiro: "))

    if numero < 0:
        print("Número inválido.")

    else:
        logaritmo = math.log(numero)
        print(f"O logaritmo de {numero} é aproximadamente {logaritmo:.4f}.")

except ValueError:
    print("Entrada inválida. Digite um número inteiro válido.")
