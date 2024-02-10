# Questão 11

nota = float(input('Digite uma nota: '))

while nota < 0 or nota > 10:
    print('Erro! Digite uma nota válida')
    nota = float(input('Digite uma nota: '))

print('Nota válida')
print(f'Nota digitada: {nota}')