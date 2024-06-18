#dicionarios sao coleções de chaves e valores
#digo a chave e ele retorna um valor. nao aceita valor duplicado
#é mutavel
#chave: valor
meses = {
    "jan":"janeiro",
    "fev":"fevereiro",
    "mar": "março",
    "abr": "abril",
    "mai": "maio",
    "jun": "junho"
}

print(meses["jan"])
print(meses.get("abr", "jan")) #se o primeiro for invalido ele retorna o segundo
print(len(meses))