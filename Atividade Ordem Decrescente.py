numero1 = int(input('Digite o primeiro número'))
numero2 = int(input('Digite o segundo número'))
numero3 = int(input('Digite o terceiro número'))

if numero1 < numero2 < numero3:
    print('Estes números estão em ordem decrescente')
elif numero1 > numero2 < numero3:
    print('Estes números não estão em ordem decrescente')
elif numero1 < numero2 > numero3:
    print('Estes números não estão em ordem decrescente')
else:
    print('Estes números não estão em ordem decrescente')
