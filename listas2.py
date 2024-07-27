nomes = ["pipoca", "mel", "amora"]

#nome1, nome2, nome3 = nomes
nome1, *resto = nomes
nome1, *_ = nomes #mais comum, significa que essa variavel não vai ser usada
print(nome1)

_, _, nome = nomes
print(nome)

#tuplas:
palavras = ("árvore", "porta-retrato", "laranja") #com ou sem ()

nomes = tuple(nomes)
nomes = list(nomes)