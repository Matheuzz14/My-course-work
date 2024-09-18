def somaImposto(taxaImposto, custo):
    custoimposto = custo + (custo * taxaImposto / 100)
    return custoimposto

taxa = float(input("Digite a taxa de imposto (em porcentagem): "))
custoinicial = float(input("Digite o custo do item antes do imposto: "))
custofinal = somaImposto(taxa, custoinicial)
print(f"O custo do item com imposto é: {custofinal}")

