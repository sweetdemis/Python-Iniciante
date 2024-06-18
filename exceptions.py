#varios exceptions pra ver como o codigo procura a expection especifica do erro que deu
try:
    numero = int(input("digite um  numero: "))
    print(numero)
    10/0
except ZeroDivisionError:
    print("divisão por zero nao é possivel")
except ValueError:
    print("tem que ser numero")
except:
    print("erro inesperado")
finally: #de erro ou nao, ele vai executar
    print("sempre executa")