condicao = True

while condicao:
    nome = input("digite seu nome: ")
    if nome == "sair":
        break
    print(f"oi, {nome}")

###############

cont = 1
while cont <= 20:
    cont*=2

    if cont == 12:
        continue

    if cont == 17:
        continue

    if cont == 19:
        break

    print(f'{cont=}')

################

nome = "sarah"
for index in nome:
    print(index)

index = 0
novo_nome = ""
while index < len(nome):
    letra = nome[index] #a letra vai receber a letra que está no index
    novo_nome += letra+"*" #a string nova vai receber o que está armazenado na variavel letra + o asterisco
    index+=1

print(novo_nome)