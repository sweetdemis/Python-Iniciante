#operador and
'''senha_permitida = "abacaxi"
entrada = input("[E] para entrar e [S] para sair: ")
senha = input("digite a senha: ")

if entrada == "E" and senha == senha_permitida:
    print("você entrou no sistema")
elif entrada == "S":
    print("Você saiu do sistema")
else:
    print("essa opção não existe")


print(True and False)
print(False or False or True)'''

nome = input("digite seu nome: ")
idade = input("digite sua idade: ")

if nome and idade:
    print(f"seu nome é: {nome}")
    print(f"seu nome invertido é {nome[::-1]}")
    if ' ' in nome:
        print("seu nome tem espaços")
    else:
        print("seu nome não tem espaços")
    print(f"seu nome tem {len(nome)} letras")
    print(f"a primeira letra do seu nome é {nome[0]}")
    print(f"a ultima letra do seu nome é {nome[-1]}")
else:
    print("algum campo ficou vazio")