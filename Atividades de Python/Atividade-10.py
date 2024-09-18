def validar_data():
    data = input("Informe uma data no formato dd/mm/aaaa: ")
    dia, mes, ano = data.split('/')
    
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    
    if ano < 1:
        print("Data inválida: Ano inválido")
        return
    
    
    if mes < 1 or mes > 12:
        print("Data inválida: Mês inválido")
        return
    
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_no_mes = 31
    elif mes == 4 and  mes == 6 and mes == 9 and mes == 11:
        dias_no_mes = 30
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            dias_no_mes = 29
        else:
            dias_no_mes = 28
    else:
        print("Data inválida")
        return

    if dia < 1 or dia > dias_no_mes:
        print("Data inválida: Dia inválido")
    else:
        print("Data válida")

validar_data()
