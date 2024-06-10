print("Qual seu sexo ? M = Masculino e F = Feminino.")
sexo_do_usuario = input("escolha M ou F")

if sexo_do_usuario =="M" or sexo_do_usuario =="m":
    print("Você é do sexo Masculino")
elif sexo_do_usuario =="F" or sexo_do_usuario =="f":
    print("Você é do sexo Feminino")
else:
    print("Valor inválido")
