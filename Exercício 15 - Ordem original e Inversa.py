lista = []

for x in range(0,10):
    if x <=9:
        entrada = int(input("Digite um número:"))
        lista.append(entrada)

print("Ordem original:",lista)

lista.reverse()
print("Ordem inversa:",lista)