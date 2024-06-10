v_fabrica = float(input("Qual o valor de fábrica deste carro ?"))

def calc_imposto_distribuidor():
    global v_fabrica
    v_com_imposto_distribuidor = v_fabrica+(v_fabrica*0.28)

    return v_com_imposto_distribuidor

def calc_impostos_gov(v):
    v += v*0.45
    return v
v_atualizado = calc_imposto_distribuidor()
v_atualizado = calc_impostos_gov(v_atualizado)

print(f"O carro de valor de fábrica:{v_fabrica} fica com um valor total ao consumidor de: {v_atualizado}")