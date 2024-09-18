def contar_digitos():
    numero = int(input("Informe um número inteiro: "))
    quantidade_digitos = len(str(abs(numero)))
    print(quantidade_digitos)

contar_digitos()
