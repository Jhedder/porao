valor_recebido = float(input("Qual o valor total da compra ?"))

def prestacoes(prestacao):
    return valor_recebido / 5
prestacao = prestacoes(valor_recebido)
print("O valor das prestações é de:",prestacao," por mês.")