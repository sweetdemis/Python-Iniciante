palavra = input("digite uma palavra: ")

vogais = "aeiouAEIOU"

contador = 0

for caractere in palavra: 
    if caractere in vogais:
        contador += 1

print(contador)