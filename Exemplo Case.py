lang = input("Qual linguagem de programação você quer aprender ?")

match lang:
    case "JavaScript":
        print("Você pode ser desenvolvedor web")
    case "Python":
        print("Você pode ser cientista de dados")
    case "PhP":
        print("Você pode ser um desenvolvedor backend")
    case "Solidity":
        print("Você pode ser um desenvolvedor Blockchain")
    case "Java":
        print("Você pode ser um desenvolvedor de aplicativos para celular")
    case _:
        print("A linguagem não importa, o que importa é resolver problemas")