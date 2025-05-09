

def verificar_maior():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num1 > num2:
            print(f"{num1} é maior que {num2}")
        elif num1 < num2:
            print(f"{num1} é menor que {num2}")
        else:
            print(f"{num1} é igual a {num2}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números.")

if __name__ == "__main__":
    verificar_maior()

# escolhi 20 e 15 que deu 20 > 15