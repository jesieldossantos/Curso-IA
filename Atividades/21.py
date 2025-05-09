
def verificar_numero():
    try:
        numero = float(input("Digite um número: "))
        if numero > 10:
            print("O número é maior que 10")
        elif numero < 10:
            print("O número é menor que 10")
        else:
            print("O número é igual a 10")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    verificar_numero()

# escolhi 17 que é maior que 10
# escolhi 8 que é menor que 10
