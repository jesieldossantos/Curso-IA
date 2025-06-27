#Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.

def verificar_numero():
    try:
        numero = float(input("Digite um número: "))
        if numero > 0:
            print("O número é positivo.")
        elif numero < 0:
            print("O número é negativo.")
        else:
            print("O número é zero.")
    except ValueError:
        print("Por favor, digite um número válido.")

verificar_numero()

#escolhi 5 e é positivo.
#escolhi -3 e é negativo.
#escolhi 0 e é zero.