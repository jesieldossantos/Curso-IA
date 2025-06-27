# Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.

nota = float(input("Digite uma nota de 0 a 10: "))
if nota < 0 or nota > 10:
    print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
elif nota < 4:
    print("Nota Baixa")
elif nota < 7:
    print("Nota Média")
else:
    print("Nota Alta")

# nota 1 e considerada baixa
# nota 5 e considerada media
# nota 8 e considerada alta