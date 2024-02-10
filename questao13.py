# Questão 13

nome = input('Digite seu nome: ')

while len(nome) < 3:
    print('O nome deve ter ao menos 3 letras!')
    nome = input('Digite seu nome: ')

idade = int(input('Digite sua idade: '))

while idade < 0 or idade >= 150:
    print('A idade deve estar entre 0 e 150!')
    idade = int(input('Digite sua idade: '))

salario = int(input('Digite seu salário: '))

while salario < 0:
    print('O salário deve ser maior que 0!')
    salario = int(input('Digite seu salário: '))

sexo = input("Digite seu sexo M ou F: ")

while sexo not in ['m', 'M', 'f', 'F']:
    print('Sexo inválido!')
    sexo = input('Digite seu sexo M ou F: ')

estado_civil = input("Digite seu estado civil: S - Solteiro(a); C - Casado(a); V - Viúvo(a); D - Divorciado(a) ")

while estado_civil not in ['s', 'c', 'v', 'd', 'S', 'C', 'V', 'D']:
    print('Estado civil inválido!')
    estado_civil = input('Digite seu estado civil: S - Solteiro(a); C - Casado(a); V - Viúvo(a); D - Divorciado(a) ')

print(f'Olá {nome}, você tem {idade} anos, tem um salário de R$ {salario}, seu sexo é {sexo.upper()} e seu estado civil é {estado_civil.upper()}')
