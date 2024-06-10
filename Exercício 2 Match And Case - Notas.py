notas = float(input("Qual foi a sua primeira nota ?"))
notas1 = float(input("Qual foi a sua segunda nota?"))
media = (notas + notas1) / 2
match media:
    case media if media >= 0.0 and  media <= 4.0:
        print("Você foi reprovado")
    case media if media >= 4.0 and  media <= 7.0:
        print("Você precisa realizar o exame")
    case media if media >= 7.1 and  media <=10.0:
        print("Você foi aprovado")
    case _:
        print("Inválido, tente novamente!")

