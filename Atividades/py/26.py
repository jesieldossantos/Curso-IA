#  Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.

def verificar_multiplos():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        if num1 % 5 == 0 and num2 % 5 == 0:
            print(f"Os números {num1} e {num2} são múltiplos de 5")
        elif num1 % 5 == 0:
            print(f"O número {num1} é múltiplo de 5, mas {num2} não é")
        elif num2 % 5 == 0:
            print(f"O número {num2} é múltiplo de 5, mas {num1} não é")
        else:
            print(f"Nenhum dos números {num1} e {num2} é múltiplo de 5")
    except ValueError:
        print("Entrada inválida. Por favor, digite números.")

if __name__ == "__main__":
    verificar_multiplos()

# escolhi 8 e 4 e nenhum deles é multiplo de 5.
# escolhi 5 e 10 e ambos são multiplos de 5.
# escolhi 7 e 10 e apenas o 10 é multiplo de 5.