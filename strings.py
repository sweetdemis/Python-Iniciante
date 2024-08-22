gato = "amora"
cachorro1 = "pipoca"
cachorro2 = "mel"

print(f"tenho uma gata chamada {gato}, e duas cachorras chamadas {cachorro1} e {cachorro2}.")
#o f na frente faz as variaveis no meio da string funcionarem. Se chama "f strings"

string = "eu amo o jao"
print(f"{string}")
print(string.upper())
print(len(string))

ostring = "MAS ENFIM ACONTECE"
print(ostring.lower())

texto = "finge que eu fui um acidente."
print(texto.capitalize()) #primeira letra maiuscula

print(string.islower()) #retorna um booleano dizendo se é ou não maiusculo
print(ostring.isupper())

print(texto.strip()) #remove espaços antes e depois, mas não entre as palavras


lista = texto.split() #separa a string, se não tiver argumento o padrão é separar onde há espaços
print(lista)

lista_unida = "-".join(lista) #vai unir de volta. para strings, listas e tuplas
print(lista_unida)

print(string.replace("jao", "louis")) #pode ser substituida uma letra ou uma palavra (substitui jao por louis)
palavra = "primeira"
print(palavra.replace("i", "e", 1)) #vai substituir o primeiro "i" que ele achar. se fosse 2, ele ia substituir o primeiro e o segundo.

print(len(string)) #tamanho da string

print(string[2]) #retorna a letra na posiçao

print(string[2:5]) #retorna os caracteres entre os números e não inclui o 5º elemento
print(string[-1:-4]) #o -1 é oultimo elemento e ele vai contar ate o -3
print(ostring[0:13:2]) #começa no 0, vai ate o 12 e pula de dois em dois
print(ostring[::-1]) #inverte    

print(string.index("a")) #retorna o indice de uma letra ou uma palavra

x = "jao" in string
print(x)

#para quebra de linha:
lista = """linha 1,
linha 2,
linha 3."""
print(lista)
#ou
listinha = "linha 1 \nlinha 2 \nlinha 3"
print(listinha)