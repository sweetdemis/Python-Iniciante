import os
os.system("cls")

lista = ["pipoca", "mel", "amora",]
lista.insert(1, "ursinho")

'''cont = 0

for nome in lista:
    print(cont, nome)
    cont+=1'''

#da forma abaixo o for só vai poder ser executado uma vez, porque é como se fosse uma variável sendo consumida, e depois acaba
lista_enumerada = enumerate(lista)
for item in lista_enumerada:
    print(item)
print("---------------")

#mas dessa forma o for poderia ser executado quantas vezes for preciso:
for item in enumerate(lista):
    print(item)
print("---------------")

#ou dessa forma:
lista_enumerada = list(enumerate(lista, start=1))
print(lista_enumerada)
#que vai gerar dois valores em uma tupla (item), então da pra desempacotar eles em duas variáveis.
for item in enumerate(lista, start=1):
    indice, valor = item
    print(f"{indice}: {valor}")
#mas para poupar linhas:
for indice, valor in enumerate(lista, start=1):
    print(f"{indice}: {valor}")