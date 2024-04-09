#Faça um programa que leia 2 notas de um aluno, verifique se as notas são validas e exiba na tela a média destas notas. 
#Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido,
# este fato deve ser informado ao usuário e o programa termina.

nota1 = float(input("Digite a primeira nota "))
while nota1 < 0.0 or nota1 > 10.0:
    print("Nota inválida. Digite um valor entre 0.0 e 10.0.")
    nota1 = float(input("Digite a primeira nota novamente: "))

nota2 = float(input("Digite a segunda nota  "))
while nota2 < 0.0 or nota2 > 10.0:
    print("Nota inválida. Digite um valor entre 0.0 e 10.0.")
    nota2 = float(input("Digite a segunda nota novamente: "))

# Calcula a média
media = (nota1 + nota2) / 2

# Exibe a média
print(f"A média das notas é: {media:.2f}")
