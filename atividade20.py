#Leia a idade e o tempo de serviço de um trabalhador e escreve se ele pode ou não se aposentar.
#As condições para aposentadoria são:
#a. Ter pelo menos 65 anos
#b. Ou ter trabalhado pelo menos 30 anos
#c. Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Digite a idade do trabalhador: "))
tempo = int(input("Digite o tempo de serviço em anos: "))

if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
    print("O trabalhador pode se aposentar.")

else:
    print("O trabalhador não pode se aposentar.")
