# Questão 10

nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))

media = (nota1 + nota2) / 2

if(media == 10.0):
    print('Aprovado com Distinção')
elif(media >= 7.0):
    print('Aprovado')
else:
    print('Reprovado')