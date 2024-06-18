import numpy as np

numeros = []

for i in range(5):
    numero = float(input("digite um valor: "))
    numeros.append(numero)

array = np.array(numeros)
print(numeros)

media = np.mean(array)

print(f"a média dos números é {media}")