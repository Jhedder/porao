distancia_total = int(input("Digite a distância total percorrida pelo carro"))
combustivel_gasto = int(input("Digite o total de combustível gasto"))

def consumo_medio(a,b):
    return distancia_total / combustivel_gasto

cons_medio = consumo_medio(distancia_total,combustivel_gasto)
print("A média  por litro do seu carro em km é:",cons_medio)

