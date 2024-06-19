class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.velocidade = 0
        self.ligado = False

    def ligar(self):
        if self.ligado:
            print("o carro já está ligado")
        else:
            print("carro ligado")
            self.ligado = True

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print("carro desligado")
        else:
            print("o carro já está desligado")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"voce está a {self.velocidade} km")
        else:
            print("primeiro ligue o carro")

    def frear(self):
        if self.velocidade > 0:
            if self.ligado:
                self.velocidade -= 1
                print(f"voce está a {self.velocidade} km")
            else:
                print("primeiro ligue o carro")
        else:
            print("voce ja está parado")