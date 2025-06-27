# Crie um algoritmo que pergunte ao usuário um número e verifique se ele é múltiplo de 3.

def verificar_multiplo():
    try:
        numero = int(input("Digite um número: "))
        if numero % 3 == 0:
            print(f"O número {numero} é múltiplo de 3")
        else:
            print(f"O número {numero} não é múltiplo de 3")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    verificar_multiplo()

# escolhi 3 e ele é multiplo de 3.
# escolhi 27 e ele é multiplo de 3.