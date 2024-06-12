class Animal:
    def __init__(self, nome: str, tipo: str, cor_da_pele: str, idade: str, raca: str):
        self.nome = nome
        self.tipo = tipo
        self.cor_da_pele = cor_da_pele
        self.idade = idade
        self.raca = raca

class Peixe(Animal):
    def __init__(self,nome: str, tipo: str, cor_da_pele: str, idade: str, raca:str, habitat: str):
        super().__init__(nome=nome, tipo=tipo, cor_da_pele=cor_da_pele, idade=idade, raca=raca)
        self.habitat = habitat

peixe = Peixe(nome="Pink", tipo="Peixe", cor_da_pele="Cinza", idade=1, raca="Colisa", habitat="Aquário")
print(f"Nome: {peixe.nome}, Tipo: {peixe.tipo}, Cor da Pele: {peixe.cor_da_pele}, Idade: {peixe.idade}, Raça: {peixe.raca}, Habitat: {peixe.habitat}")