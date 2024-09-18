def ehprimo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

def primosate(n):
    primos = []
    for i in range(1, n + 1):
        if ehprimo(i):
            primos.append(i)
    return primos

n = int(input("Digite um número inteiro positivo: "))
print(f"Números primos de 1 até {n}: {primosate(n)}")
