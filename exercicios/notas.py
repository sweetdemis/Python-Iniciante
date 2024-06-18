import numpy as np

valores = []

for i in range(10):
        valor = float(input(f"digite o {i+1}° valor: "))
        valores.append(valor)

array = np.array(valores)
print(array)

soma = np.sum(array)
media = np.mean(array)
dp = np.std(array)
maior = np.max(array)
menor = np.min(array)
print(f"média: {media}")
print(f"soma: {soma}")
print(f"desvio padrão: {dp}")
print(f"menor número: {menor}")
print(f"maior número: {maior}")