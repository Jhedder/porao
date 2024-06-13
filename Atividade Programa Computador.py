class Computador:
    def __init__(self, cpu: str, qtd_memoria: int, ligado: bool):
        self.cpu = cpu
        self.qtd_memoria = qtd_memoria
        self.ligado = True

    def ligar(self):
        self.ligado = True
        print("O computador foi ligado.")

    def desligar(self):
        self.ligado = False
        print("O computador foi desligado.")

class PCGamer(Computador):
    def __init__(self, jogando: bool):
        self.jogando = jogando
    def iniciar_jogo(self):
        self.jogando = True
        print("O jogo foi iniciado.")
    
    def fechar_jogo(self):
        self.jogando = False
        print("O jogo foi fechado.")

computador1 = Computador(cpu="Intel Core i9", qtd_memoria="32GBRAM", ligado=True)
computador1.ligar()
computador1.desligar()

computadorgamer = PCGamer(Computador)
computadorgamer.iniciar_jogo()
computadorgamer.fechar_jogo()
computadorgamer.desligar()
