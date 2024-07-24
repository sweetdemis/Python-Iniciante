i = 1

while i <= 10:
    print(i)
    i += 1


bichinhos = ["pipoca", "mel", "amora"]
for item in bichinhos:
    print(item)

palavra = "fubanga" #se a palavra estivesse entre [], seria impressa a palavra, como em bichinhos
for letra in palavra:
    print(letra)

for index in range(20): #numera numeros. nao pega o ultimo
    print(index)

for index in range(17, 20): #imprime do 17 ate o 19
    print(index)

for index in range(12, 20, 2): #o ultimo numero é de quantos em quantos
    print(index)

for index in range(100, 0, -2): #de trás para frente
    print(index)

for index in range(len(bichinhos)):
    print(index, "->", bichinhos[index])

for index in range(5):
    if index == 0:
        print("primeira linha")
    else:
        print(f"outras linhas {index}")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for linha in matriz:
    #print(linha)
    print("----")
    for coluna in linha:
        print(coluna)