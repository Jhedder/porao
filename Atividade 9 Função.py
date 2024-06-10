valor_depositado = 0
valor_depositado += float(input(f"Qual valor será depositado e irá render 0.70% a.m"))

def rendimento_depois_de_1mes(v):
    v *= 0.0070 #isso dá 0.70%
    return v
v_rendido = rendimento_depois_de_1mes(valor_depositado)
v_total = valor_depositado + v_rendido
print("depois de 1 mês, seu valor",valor_depositado,"rendeu:",v_rendido,"dando um total de:",v_total)