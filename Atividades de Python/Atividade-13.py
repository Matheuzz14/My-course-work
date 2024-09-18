valor_saque = int(input("Digite o valor que deseja sacar (entre 10 e 600 reais): "))

if valor_saque < 10 or valor_saque > 600:
    print("Valor inválido. O valor do saque deve estar entre 10 e 600 reais.")
else:
    notas100 = valor_saque // 100
    valor_saque %= 100

    notas50 = valor_saque // 50
    valor_saque %= 50

    notas10 = valor_saque // 10
    valor_saque %= 10

    notas5 = valor_saque // 5
    valor_saque %= 5

    notas1 = valor_saque

    print(f"Para sacar a quantia de {valor_saque} reais, serão fornecidas:")
    if notas100 > 0:
        print(f"{notas100} nota(s) de 100 reais")
    if notas50 > 0:
        print(f"{notas50} nota(s) de 50 reais")
    if notas10 > 0:
        print(f"{notas10} nota(s) de 10 reais")
    if notas5 > 0:
        print(f"{notas5} nota(s) de 5 reais")
    if notas1 > 0:
        print(f"{notas1} nota(s) de 1 real")
