familia = ["sarah", "pipoca", "mel", "amora"]   

print(familia[1]) 

print(familia[-1]) #ultimo item

print(familia[1:])

print(familia[1:3]) #nao pega o indice 3, tambem nao sei pq

palavras = ["abajur", "bola", "cachorro", "dado", "estrada"]
palavras[3] = "dondoca"
#print(palavras)

palavras.extend(["farofa", "gago"]) #mais de uma palavra, no final da lista
palavras.append("helicoptero") #apenas uma palavra
palavras.insert(1, "boboca") #escolhe o indice
palavras.pop() #remove o ultimo
palavras.remove("bola")
del palavras[0]
#palavras.clear()
print(palavras.index("dondoca")) #retorna o indice
print(palavras.count("gago")) #numero de vezes em que aparece
print(palavras)

idade_familia = [19, 9, 7, 1]
print(idade_familia)
idade_familia.sort() #organiza em ordem crescente
print(idade_familia)

familia.sort() #tambem organiza as strings
familia.reverse() #de traz pra frente
print(familia) 

familia2 = familia.copy() #nao existe outra lista, a segunda ta só referenciando a primeira; mesmo espaço de memoria
print(familia2)
familia.remove("sarah")
print(familia2) 

familia3 = familia.copy() #uma lista nova, mas igual a outra
familia.remove("pipoca")
print(familia3)

texto = "abacaxi, banana, cenoura, damasco"
lista = texto.split(", ")
for index, item in enumerate(lista, start=1):
    print(f"{index}: {item}")

#listas dentro de listas:
salas = [
    ["Harry", "Zayn", (0, 10, 20, 30, 40, 50)],
    ["Niall", "Louis", "Liam"]
]

print(salas[1])
print(salas[1][1])
print(salas[0][2][2])

print(*salas, sep="\n")