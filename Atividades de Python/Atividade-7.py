def calculareajuste():
    salarioatual = float(input("Informe o salário atual do colaborador: "))
    
    if salarioatual <= 280:
        percentualreajuste = 20
    elif salarioatual <= 700:
        percentualreajuste = 15
    elif salarioatual <= 1500:
        percentualreajuste = 10
    else:
        percentualreajuste = 5
    
    valoraumento = salarioatual * (percentualreajuste / 100)
    novosalario = salarioatual + valoraumento
    
    print(f"Salário antes do reajuste: R${salarioatual:.2f}")
    print(f"Percentual de aumento aplicado: {percentualreajuste}%")
    print(f"Valor do aumento: R${valoraumento:.2f}")
    print(f"Novo salário após o aumento: R${novosalario:.2f}")

calculareajuste()
