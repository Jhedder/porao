lista = ["Maça","Banana","Morango","Abacaxi","Goiaba","Laranja","Pera","Pessego","Melancia","Manga"]
def remover_itens():
    global lista
    print(lista)
    if len(lista) >0:
        lista.pop()
        remover_itens()
    else:
        print("Esta Lista Está Vazia")
        
remover_itens()