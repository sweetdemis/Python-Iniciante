import numpy as np

valores = []

for i in range(6):
    valor = int(input(f"digite o {i+1}° valor: "))
    valores.append(valor)

array = np.array(valores)
array.sort()

for index in array:
    print(index)