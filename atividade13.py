# A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10,
#respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. 
#A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de laboratório: 2; Avaliação Semestral: 3; Exame Final: 5.
#De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.


trabalho_lab = float(input("Digite a nota do trabalho de lab "))
avaliacao_semestral = float(input("Digite a nota da avaliação semestral: "))
exame_final = float(input("Digite a nota do exame final: "))

media_final = (2 * trabalho_lab + 3 * avaliacao_semestral + 5 * exame_final) / 10

if 0 <= media_final < 3:
    print("Aluno reprovado.")

elif 3 <= media_final < 5:
    print("Aluno em recuperação.")
    
else:
    print("Aluno aprovado.")
