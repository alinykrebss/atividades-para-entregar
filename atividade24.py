#A tarifas de certo parque de estacionamento são as seguintes:a. 1ª e 2ª hora – R$ 1,00 cadab. 3ª e 4ª hora – R$ 1,40 cadac. 5ª hora e seguintes R$ 2,00 cada
#O numero de horas a pagar é sempre inteiro arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minutos.
#Os momentos de chegada ao parque e partida são apresentados na foram de pares de inteiros, representando horas e minutos.
#Por exemplo, o par 12 50 representará “dez para a uma da tarde”.
#Pretende-se criar um programa que, lidos pelo teclado s momento de chegada e de partida, 
#escreva na tela o preço cobrado pelo estacionamento.
#Admite-se que a chega e a partida se dão com intervalor não superior a 24 horas.
#Portanto, se uma dada hora dechegada for superior à partida, isso não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.


chegada_hora, chegada_minuto = map(int, input("Digite o momento de chegada (hora minuto): ").split())
partida_hora, partida_minuto = map(int, input("Digite o momento de partida (hora minuto): ").split())

tempo_chegada = chegada_hora * 60 + chegada_minuto
tempo_partida = partida_hora * 60 + partida_minuto
tempo_total = tempo_partida - tempo_chegada

if tempo_total <= 120:
    preco = 1.00
elif tempo_total <= 240:
    preco = 1.40
else:
    preco = 2.00

print(f"Preço cobrado pelo estacionamento: R$ {preco:.2f}")
