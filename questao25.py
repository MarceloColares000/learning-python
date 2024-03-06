# Questão 25

def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo_com_imposto = custo + imposto
    return custo_com_imposto

taxaImposto = float(input("Digite a taxa de imposto: "))
custo = float(input("Digite o custo do item antes do imposto: "))

custo_com_imposto = somaImposto(taxaImposto, custo)

print("O custo do item incluindo o imposto é:", custo_com_imposto)
