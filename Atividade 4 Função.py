nome_do_vendedor = str(input("Digite o nome do Vendedor"))
salario_fixo = int(input(f"Digite o salário fixo do vendedor"))
total_vendas_efetuadas = int(input("Qual o total de vendas no mês ?"))

def calc_comissao(vendas):
    return vendas*0.15

comissao = calc_comissao(total_vendas_efetuadas)

print("O salário no final do mês foi de:",salario_fixo+comissao,". Seu salário base era de:",salario_fixo)

