#Determine se um determinado ano lido é bissexto.
#Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996

ano = float(input("me informe um ano "))

if (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
    print(" eh bissexto")

else:
 print ("nao eh bissexto")
 