# Questão 14

populacao_A = 80000
taxa_crescimento_A = 0.03  # 3% de taxa de crescimento anual
populacao_B = 200000
taxa_crescimento_B = 0.015  # 1.5% de taxa de crescimento anual
anos = 0

while populacao_A <= populacao_B:
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B
    anos += 1

print(f'Após {anos} anos, a população do país A ultrapassará ou igualará a população do país B.')
