op = int(input("escolha uma opção: \n1- celsius para fahrenheit \n2- fahrenheit para celsius\n"))

if op != (1 and 2):
        print("digite uma opção válida")

if op == 1:
    temp = float(input("digite a temperatura: "))
    temp_convertida = temp*1.8+32
    print(f"o resultado é {temp_convertida}")
elif op == 2: 
    temp = float(input("digite a temperatura: "))
    temp_convertida = (temp-32)*5/9
    print(f"o resultado é {temp_convertida}")