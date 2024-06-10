import os


def recursiva():
    entrada = str(input("Digite uma frase poética."))
    if entrada == "":
        print("Você saiu por não escrever uma frase poética.")
        arquivo = open("atividade_escrita/frases.txt","r")
        print(arquivo.read())
        arquivo.close()
        pass #avisa pra recursiva que nao vai dar em nada e sai

    if os.path.exists("atividade_escrita/frases.txt"):
        arquivo = open("atividade_escrita/frases.txt","a")
    else:
        arquivo = open("atividade_escrita/frases.txt","w")
    arquivo.write(f"{entrada}\n")
    arquivo.close()
    recursiva()

recursiva()