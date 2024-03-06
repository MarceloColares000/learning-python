# Questão 21

n = int(input("Digite um número inteiro: "))

for i in range(1, n + 1):
    linha = " ".join([str(i)] * i)
    print(linha)
