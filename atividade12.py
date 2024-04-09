#2. Faça um algoritmo que calcule a média ponderada das notas de 2 provas.
# A primeira prova tem peso 1 e a segunda tem peso 2.
# Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
# A nota para aprovação deve ser igual o superior a 70 pontos.


nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))


media = (nota1 + 2 * nota2) / 3


if media >= 70:
    print(f"Média: {media:.2f} - Aprovado")
    
else:
    print(f"Média: {media:.2f} - Reprovado")
