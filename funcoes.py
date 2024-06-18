def big_mac():
    print("sanduiche big mac")

#big_mac() #chamando a funçao

def fazer_big_mac(nome):
    print(f"sanduiche big mac de {nome}")

#fazer_big_mac("sarah")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante(tipo, tamanho):
    print(f"{tipo}, {tamanho}")

def combo(nome, tipo_refri, tamanho_refri, tamanho_batata):
    fazer_big_mac(nome)
    preparar_refrigerante(tipo_refri, tamanho_refri)
    fazer_batata(tamanho_batata)

#combo("sarah", "sprite", "pequeno", "grande") 

####################################

def soma_numero(num1, num2):
    return num1+num2

resultado = soma_numero(15, 20)
print(resultado)

def maior_num(lista_num):
    lista_num.sort() #ordenou do menor para o maior
    lista_num.reverse() #reverteu, entao ficou do maior para o menor
    maior_num = lista_num[0] #mostra o 1 numero
    return maior_num

resultado = maior_num([23, 8, 78, 94, 32, 11]) #aqui ta chamando a funçao

print(resultado)