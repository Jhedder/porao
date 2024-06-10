import random

numero_sorteado = random.randint(1,10)

numero_do_usuario = None
tentativas = 0

while numero_sorteado != numero_do_usuario:
    numero_do_usuario = int(input("Digite o número entre 1 e 10:"))
    tentativas += 1
    if numero_do_usuario >=1 and numero_do_usuario <=10:
        if numero_sorteado< numero_do_usuario:
         print("Tente um número menor na próxima vez")
        else:
         print("tente um número maior na próxima")
    else:
        print("Valor inválido")

print("O seu número foi:" ,numero_do_usuario, "e o número sorteado foi: ",numero_sorteado, "Suas tentativas foram" ,tentativas)