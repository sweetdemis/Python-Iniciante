nome = "amora"
animal = "gato"
idade = "1"

string = "{} é um {} e tem {} ano"
formato = string.format(nome, animal, idade)

print(formato)

horas = 3+7+3+2+6+12+9+11+11
print(horas)

primeiro = input("digite o primeiro valor: ")
segundo = input("digite o segundo valor: ")

if primeiro > segundo:
    print(f"o primeiro número {primeiro} é maior que o segundo número {segundo}")
else:
    print(f"o segundo numero {segundo} é maior que o primeiro número {primeiro}")

try:
    numero = int(input("digite um número: "))
    if numero % 2 == 0:
        print("o número é par")
    else:
        print("o número é ímpar")

except ValueError:
    print("precisa ser um número inteiro")

hora = int(input("que horas são agora? "))
if hora <= 11:
    print("bom dia!")
elif hora >= 12 and hora <= 17:
    print("boa tarde!")
elif hora > 17:
    print("boa noite!")
else: 
    print("hora inválida")

nome = input("qual o seu nome? ")

if len(nome) <=4:
    print("seu nome é pequeno")
elif len(nome) == 5 or len(nome) == 6:
    print("seu nome é normal")
elif len(nome) > 6:
    print("seu nome é bem grande")



    