numero = 1
max = int(input("Digite um inteiro maior que 1:"))
print("Numeros ímpares entre 1 e", max, ":")
while numero <= max:
    if numero%2==1:
        print(numero, end=" ")
    numero+=1