#Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente pelos dois.

num = int(input("Digite um número "))


divisivel_3 = num % 3 == 0
divisivel_5 = num % 5 == 0

if divisivel_3 and divisivel_5:
    print(f"{num} é divisível por 3 e por 5 simultaneamente.")
elif divisivel_3:
    print(f"{num} é divisível por 3, mas não por 5.")
elif divisivel_5:
    print(f"{num} é divisível por 5, mas não por 3.")
else:
    print(f"{num} não é divisível por 3 nem por 5.")
