# Questão 19

caracteres = []

for i in range(10):
    caracter = input(f"Digite o {i+1}º caractere: ")
    caracteres.append(caracter)

vogais = ['a', 'e', 'i', 'o', 'u']

num_consoantes = 0

consoantes = []

for caracter in caracteres:
    if caracter.isalpha() and caracter.lower() not in vogais:
        num_consoantes += 1
        consoantes.append(caracter)

print(f"Foram lidas {num_consoantes} consoantes.")
print("Consoantes lidas:", ', '.join(consoantes))
