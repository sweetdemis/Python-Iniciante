import numpy as np

numeros = []

for i in range(5):
    numero = int(input(f"digite o {i+1}° valor: "))
    numeros.append(numero)

array = np.array(numeros)
maior = array.max()
print(f"o maior número é {maior}")