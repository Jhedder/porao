passaros = ["arara","papagaio","sabiá","canário","beija-flor","joão-de-barro"]
passaros.pop(-1) #deleta um índice e o seu valor, obviamente.
print(passaros)

passaros.append("Rolinha")#adiciona esse valor no final da lista.
print(passaros)
passaros.insert(0,"angribird_vermelho") #substitui ou insere esse valor no índice zero.
print(passaros)
passaros.remove("papagaio") #remove buscando o valor
print(passaros)

passaros[0] = "" #atribui um valor ao indice zero ou substitui o anterior




