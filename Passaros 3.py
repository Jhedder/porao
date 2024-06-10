passaros = ["arara","papagaio","sabiá","canário","beija-flor","joão-de-barro"]

print(passaros)
print("  ")
print(" abaixo a lista passaro em ordem reversa")
passaros.reverse() #não retorna exibição, só usado para manipulação.
print(passaros)

if "beija-flor" in passaros: #usamos o in para localizar um valor na lista.
    print("acharam o beija-flor")
else:
    print("o beija-flor não está")


passaros.pop(-1) #deleta um índice e o seu valor, obviamente.
print(passaros)

passaros.append("Rolinha")#adiciona esse valor no final da lista.
print(passaros)
passaros.insert(0,"angribird_vermelho") #substitui ou insere esse valor no índice zero.
print(passaros)
passaros.remove("papagaio") #remove buscando o valor
print(passaros)

passaros[0] = "" #atribui um valor ao indice zero ou substitui o anterior


