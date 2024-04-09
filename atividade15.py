#Usando switch, escreva um programa que leia um inteiro entre 1 e 12 
#e imprima o mês correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.

numero_mes = int(input("Digite um número entre 1 e 12: "))

if 1 <= numero_mes <= 12:
    meses_ano = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    print(f"O mês correspondente é {meses_ano[numero_mes - 1]}.")
    
else:
    print("Número inválido.")
