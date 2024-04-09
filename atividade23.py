#Escreva um programa que, dada a idade de um atleta da categoria bocha rolada em cancha de terra, classifique-o em uma das seguintes categorias:
#Categoria
#Idade
#Infantil A 5 a 7
#Infantil B 8 a 10
#Juvenil A 11 a 13
#Juvenil B 14 a 17
#Sênior Maiores de 18 anos


idade = int(input("Digite a idade do atleta: "))

if 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 10:
    categoria = "Infantil B"
elif 11 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
else:
    categoria = "Sênior "

print(f"O atleta está na categoria: {categoria}")
