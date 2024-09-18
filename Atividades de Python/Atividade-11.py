numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000:
    print("Número fora do intervalo permitido.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    tem_centenas = centenas != 0
    tem_dezenas = dezenas != 0
    tem_unidades = unidades != 0

    if tem_centenas:
        if tem_dezenas and tem_unidades:
            print(f"{numero} = {centenas} centena{'s' if centenas > 1 else ''}, {dezenas} dezena{'s' if dezenas > 1 else ''} e {unidades} unidade{'s' if unidades > 1 else ''}")
        elif tem_dezenas:
            print(f"{numero} = {centenas} centena{'s' if centenas > 1 else ''} e {dezenas} dezena{'s' if dezenas > 1 else ''}")
        elif tem_unidades:
            print(f"{numero} = {centenas} centena{'s' if centenas > 1 else ''} e {unidades} unidade{'s' if unidades > 1 else ''}")
        else:
            print(f"{numero} = {centenas} centena{'s' if centenas > 1 else ''}")
    elif tem_dezenas:
        if tem_unidades:
            print(f"{numero} = {dezenas} dezena{'s' if dezenas > 1 else ''} e {unidades} unidade{'s' if unidades > 1 else ''}")
        else:
            print(f"{numero} = {dezenas} dezena{'s' if dezenas > 1 else ''}")
    elif tem_unidades:
        print(f"{numero} = {unidades} unidade{'s' if unidades > 1 else ''}")
    else:
        print(f"{numero} = 0 unidades")
