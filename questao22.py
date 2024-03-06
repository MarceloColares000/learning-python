# Questão 22

n = int(input("Digite um número inteiro: "))

for i in range(1, n + 1):
    linha = " ".join(map(str, range(1, i + 1)))
    print(linha)
