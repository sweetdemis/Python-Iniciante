import math
a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

delta = ((b*b) - (4*a*c))
raiz = math.sqrt(delta)

x1 = (-b+raiz)/2*a

x2 = (-b-raiz)/2*a

print(f"as opções são {x1} e {x2}")