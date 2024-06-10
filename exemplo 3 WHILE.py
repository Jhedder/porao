# Pedindo entrada do usuário até que a entrada seja "sair"
entrada = ""
while entrada != "sair":
    entrada = input("Digite algo(ou 'sair' para sair): ")
    print("Você digitou:", entrada)