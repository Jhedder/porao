class Carro:
    def __init__(self, marca, modelo, cor_do_carro, potencia, preco):
        self.marca = marca
        self.modelo = modelo
        self.cor_do_carro = cor_do_carro
        self.potencia = potencia
        self.preco = preco

carro1 = Carro("Toyota","Lexus RX","Cinza",371,580000)
print(carro1.marca)
print(carro1.modelo)
print(carro1.cor_do_carro)
print(carro1.potencia)
print(carro1.preco)
            
