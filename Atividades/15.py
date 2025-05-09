#Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 17 anos).

idade = int(input("Digite sua idade: "))

if idade >= 13 and idade <= 17:
    print("Você é adolescente.")
else:
    print("Você não é adolescente.")

# escolhi 12 que não é adolescente
# escolhi 15 que é adolescente