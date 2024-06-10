lista = ["Maça","Banana","Morango","Abacaxi","Goiaba","Laranja","Pera","Pessego","Melancia","Manga"]
def remover_itens(l:list):
    
    print(l)
    if len(l) >0:
        l.pop()
        remover_itens(l)
    else:
        print("Esta Lista Está Vazia")
        
remover_itens(lista)