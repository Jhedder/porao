frases = []
def adicionar_frases():
    print("Adicione uma frase, caso você não digitar nada, o programa será encerrado.")
    entrada = input("Digite aqui: ")
    if entrada == "":
        print("Você não digitou nada, portanto, o programa será encerrado.")
        print(frases)
    else:
        frases.append(entrada)
        adicionar_frases()

adicionar_frases()

