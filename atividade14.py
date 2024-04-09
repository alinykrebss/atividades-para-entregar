#Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a 
#este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

num_dia = int(input("Digite um número entre 1 e 7: "))


if 1 <= num_dia <= 7:
    dias_semana = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]
    print(f"O dia correspondente é {dias_semana[num_dia - 1]}.")

else:
    print("Número inválido.")
