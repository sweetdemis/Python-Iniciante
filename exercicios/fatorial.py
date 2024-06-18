num = int(input("digite um número: "))

count = 1
resultado = 1

while count <= num:
    resultado *= count
    count += 1

print(resultado)

#o contador vai aumentar em 1 e vai multiplicar em resultado
#exemplo numero 4:
#resultado * 1; count = 1; 
#count = 2; resultado = 2;
#count = 3; resultado = 6;
#count = 4; resultado = 24.