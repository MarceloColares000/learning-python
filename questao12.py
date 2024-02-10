# Questão 12

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

while senha  == usuario:
    print('A senha não pode ser igual ao seu nome de usuário! Tente novamente!')
    senha = input("Digite sua senha: ")

print('Conta criada! Bem vindo!')