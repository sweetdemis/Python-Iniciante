num1 = 10
num2 = 5
print(num1)
print(type(num1))

a = float(num1)
print(a)
print(type(a))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print("a",num1 % num2) #resto da divisao
print(num1 ** num2) #exponenciacao
print(num1 // num2) #divisao arredondada

print(3 + 5 * 7 + 3)
print((3 + 5) * (7 + 3))

print(abs(-15)) #retorna o valor absoluto
print(pow(3, 2)) #exponenciacao tambem
print(min(2, 4, 1, 6))
print(max(2, 4, 6, 1, 8))

print(round(3.3)) #arredonda para cima e para baixo

print(f"{60.9000:.2f}") #escolhe quantas casas aparcem depois do ponto

import math

print(math.floor(8.9)) #arredonda para baixo
print(math.ceil(2.1)) #arredonda para cima
print(math.sqrt(9)) #raiz quadrada

import decimal

num1 = decimal.Decimal("0.1")
num2 = decimal.Decimal("0.7")
print(num1 + num2) #o resultado vai ser "0.8", se não estivesse arredondado pela biblioteca
#seria um número diferente (7.9999...). mas o decimal corrige esse "erro"