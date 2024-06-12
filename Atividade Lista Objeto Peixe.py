class Peixes:
    def __init__(self, especie, tipo_de_agua, profundidade_encontrada):
        self.especie = especie
        self.tipo_de_agua = tipo_de_agua
        self.profundidade_encontrada = profundidade_encontrada
    
    def __repr__(self):
        return f"Peixe(especie='{self.especie}, tipo de agua={self.tipo_de_agua}, profundidade encontrada={self.profundidade_encontrada})" 
    
peixe1 = Peixes("Betta", "Água de baixa dureza", "Rios e Áreas Alagadiças")
peixe2 = Peixes("Peixe-Palhaço", "Águas calmas e pouco profundas", "Profundidade de 3 a 15m")
peixe3 = Peixes("Peixe-Dourado","Água Doce", "Profundidade de 20, 30 e até 150m")
peixe4 = Peixes("Salmão", "Águas Doces e Salgadas", "Profundidade de 10 30m")
peixe5 = Peixes("Tilápia", "Águas Salgadas", "Profundidade de 60 a 80m")

lista_peixes = [peixe1, peixe2, peixe3, peixe4, peixe5]

for peixe in lista_peixes:
    print(f"Peixe Especie: {peixe.especie}. Tipo de Água: {peixe.tipo_de_agua}. Profundidade Encontrada: {peixe.profundidade_encontrada}.")