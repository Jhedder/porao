sexo_do_individuo = str(input("Qual o seu sexo? M ou F ?"))#M
idade_contribuicao_inicial = int(input("Com que idade você começou a contribuir ?"))#30
idade_contribuicao_projetada_m = 65 - idade_contribuicao_inicial
idade_contribuicao_projetada_f = 62 - idade_contribuicao_inicial
if sexo_do_individuo == "M" or sexo_do_individuo == "m":
    if idade_contribuicao_projetada_m >= 25 and idade_contribuicao_projetada_m <=29:
        print(f"você tem direito a 70% do beneficio")
    elif  idade_contribuicao_projetada_m >= 30 and idade_contribuicao_projetada_m <=34: 
        print(f"Você tem direito a 77,5% do benefício")
    elif  idade_contribuicao_projetada_m >= 35 and idade_contribuicao_projetada_m <=39:
        print(f"Você tem direito a 87,5% do benefício")
    elif idade_contribuicao_projetada_m >= 40:
        print(f"Você tem direito a 100% do benefício")
    else:
        print("Você não atingiu o tempo mínimo de contribuição. Você possui apenas",idade_contribuicao_projetada_m,"de contribuição")

if sexo_do_individuo == "F" or sexo_do_individuo == "f":
    if idade_contribuicao_projetada_f >= 25 and idade_contribuicao_projetada_f <= 29:
        print(f"Você tem direito a 70% do benefício")
    elif idade_contribuicao_projetada_f >= 30 and idade_contribuicao_projetada_f <= 34:
        print(f"Você tem direito a 77,5% do benefício")
    elif idade_contribuicao_projetada_f >= 35 and idade_contribuicao_projetada_f <= 39:
        print(f"Você tem direito a 87,5% do benefício")
    elif idade_contribuicao_projetada_f >= 40:
        print(f"Você tem direito a 100% do benefício")
    else:
        print(f"Você não atingiu o tempo mínimo de contribuição. Você possui apenas",idade_contribuicao_projetada_f,)

def calc_aposentadoria(i):
    i = idade_contribuicao_inicial+40
    return i

