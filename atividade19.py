#Dados três valores A, B, C, verificar se eles podem ser valores dos lados de um triangulo e se forem,
#se é um triangulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
#a.O comprimento de cada lado de um triangulo é menor que a soma dos outros dois lados.
#b. Chama-se equilátero o triangulo que tem três lado iguais.
#c. Denominam-se isósceles o triangulo que tem o comprimento de dois lados iguais
#d. Recebe o nome de escaleno o triangulo que tem os três lados diferentes.

A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))

if A + B > C and A + C > B and B + C > A:
    if A == B == C:
        print("Triângulo equilátero (três lados iguais).")
    elif A == B or A == C or B == C:
        print("Triângulo isósceles (dois lados iguais).")
    else:
        print("Triângulo escaleno (três lados diferentes).")
else:
    print("Não é possível formar um triângulo com esses valores.")
