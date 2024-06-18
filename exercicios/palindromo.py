palavra = input("digite uma palavra: ")

palavr = palavra[::-1]

if palavr == palavra:
    print(f"a palavra {palavra} é palíndroma")
else:
    print(f"as palavras {palavra} e {palavr} não são palíndromas")