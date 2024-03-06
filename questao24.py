# Questão 24

def verificar(num):
    if num > 0:
        return 'Positivo'
    else:
        return 'Negativo'

num = float(input("Digite um número: "))

resultado = verificar(num)

print("O número é:", resultado)
