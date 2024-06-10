print("Nota Final Do Aluno")
nota = float(input("Digite a sua Nota Final"))

if nota < 6.0:
    print("Sua nota final foi F")
elif nota >= 6.0 and nota <= 7.0:
    print("Sua nota final foi D")
elif nota >= 7.0 and nota <= 8.0:
    print("Sua nota final foi C")
elif nota >= 8.0 and nota <= 9.0:
    print("Sua nota final foi B")
else:
    print("Sua nota final foi A")



