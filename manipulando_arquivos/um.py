#open("caminho", "r")

#modos:
#r - leitura
#a - append/incrementar
#w - escrita
#x - criar arquivo
#r+ - leitura e escrita
#a diferença entre a e w é que o a adiciona e o w limpa oq ja foi escrito

#arquivo = open("manipulando_arquivos/test.txt", "r")

#print(arquivo.readable()) #retorna se o arquivo pode ser lido
#print(arquivo.read()) #le o arquivo
#print(arquivo.readline()) #le a primeira linha
#print(arquivo.readline())
#print(arquivo.readline())

#lista = arquivo.readlines() #coloca os itens em uma lista
#print(lista)
#print(lista[3])

#arquivo = open("manipulando_arquivos/test.txt", "a")
#arquivo.write("\npascal\n")

#arquivo = open("manipulando_arquivos/test2.txt", "w")
#arquivo.write("pascal")

#arquivo = open("manipulando_arquivos/tes3.txt", "x")
#arquivo.write("sql")

#arquivo.close() #sempre fechar o arquivo para evitar erros

import os #para remover arquivos

if os.path.exists("manipulando_arquivos/test2.txt"):
    os.remove("manipulando_arquivos/test2.txt")
else:
    print("o arquivo ja foi removido")

#as duas fazem a mesma coisa

try:
    os.remove("manipulando_arquivos/test2.txt")
except:
    print("o arquivo ja foi removido")

os.rmdir("manipulando_arquivos/novapasta") #so remove se a pasta estiver vazia