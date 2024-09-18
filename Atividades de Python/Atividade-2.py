import random
simulacoes = 1000000
contagens = {i: 0 for i in range(1, 7)}
for _ in range(simulacoes):
    numero = random.randint(1, 6)
    contagens[numero] += 1
probabilidades = {numero: contagem / simulacoes for numero, contagem in contagens.items()}

print("Contagens:", contagens)
print("Probabilidades:", probabilidades)
