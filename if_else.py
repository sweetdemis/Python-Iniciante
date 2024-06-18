esta_frio = False
if esta_frio:
    print("veste um casaco")
else: 
    print("nao precisa de casaco")

    #operadores logicos: or, and e not()

sede = False
fome = False
dieta = False

#if sede or fome: #um ou o outro
#    print("vai na cozinha")
#else: 
#    print("fica na sala")

if sede and fome: #os dois 
    print("fazer um sanduiche e uma coquinha")
elif sede and not(fome):
    if dieta:
        print("pegar agua")
    else: 
        print("pegar uma coquinha")
elif fome and not(sede):
    print("fazer um sanduiche")
else:
    print("fazer outra coisa")


#operadores de comparaçao: ==, !=, <, >, <=, >=
num1 = "sarah"
num2 = "sara"

if num1 == num2:
    print("eles sao iguais")
#elif num1 != num2:
#    print("sao diferentes") 
elif num1 > num2:
    print("o primeiro numero é maior")
elif num1 < num2:
    print("o segundo numero é maior")