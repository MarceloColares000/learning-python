# Questão 15

populacao_A = float(input("População do país A: "))
taxa_crescimento_A = float(input("Taxa de crescimento do país A (%): ")) / 100
populacao_B = float(input("População do país B: "))
taxa_crescimento_B = float(input("Taxa de crescimento do país B (%): ")) / 100

if populacao_A <= 0 or populacao_B <= 0 or taxa_crescimento_A <= 0 or taxa_crescimento_B <= 0:
    print("Insira valores positivos.")

anos = 0
while populacao_A <= populacao_B:
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B
    anos += 1

print(f'Após {anos} anos, a população do país A ultrapassará ou igualará a população do país B.')
