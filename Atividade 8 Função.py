dolares = float(input("Quantos Dólares Você quer trocar por reais?"))
cotacao = float(input("Qual a cotação do dolar hoje?"))

def conversao_dolar_reais(d,c):
    return dolares*cotacao

conversao = conversao_dolar_reais(dolares,cotacao)

print("O valor em $US",dolares,"ficaria R$",conversao,"em reais")