# Questão 20

numeros = []
pares = []
impares = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números Pares:", pares)
print("Números Ímpares:", impares)
print("Todos os Números:", numeros)
