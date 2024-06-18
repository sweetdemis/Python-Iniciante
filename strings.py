gato = "amora"
cachorro1 = "pipoca"
cachorro2 = "mel"

print(f"tenho uma gata chamada {gato}, e duas cachorras chamadas {cachorro1} e {cachorro2}.")
#o f na frente faz as variaveis no meio da string funcionarem. Se chama "f strings"

string = "eu amo o jao"
print(f"{string}")
print(string.upper())

ostring = "MAS ENFIM ACONTECE"
print(ostring.lower())

texto = "finge que eu fui um acidente."
print(texto.capitalize()) #primeira letra maiuscula

print(string.islower()) #retorna um booleano dizendo se é ou não maiusculo
print(ostring.isupper())

print(texto.strip()) #remove espaços antes e depois, mas não entre as palavras

print(string.replace("jao", "louis")) #pode ser substituida uma letra ou uma palavra
palavra = "primeira"
print(palavra.replace("i", "e", 1)) #vai substituir o primeiro "i" que ele achar. se fosse 2, ele ia substituir o primeiro e o segundo.

print(len(string)) #tamanho da string

print(string[2]) #retorna a letra na posiçao

print(string[2:5]) #retorna os caracteres entre os números e não inclui o 5º elemento
print(string[-1:-4]) #o -1 é oultimo elemento e ele vai contar ate o -3

print(string.index("a")) #retorna o indice de uma letra ou uma palavra

x = "jao" in string
print(x)

lista = """linha 1,
linha 2,
linha 3."""
print(lista)
#ou
listinha = "linha 1 \nlinha 2 \nlinha 3"
print(listinha)