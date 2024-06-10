numero = 1
max = int(input("Digite um número máximo para o laço WHILE"))

print("Numeros pares entre 1 e", max)

while numero<= max:
    if numero%2==0:
        print(numero, end=" ")
    numero+=1