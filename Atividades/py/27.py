# Crie um programa que solicite ao usuário três números e exiba o maior deles.
def encontrar_maior():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        maior = max(num1, num2, num3)
        print(f"O maior número é {maior}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números.")

if __name__ == "__main__":
    encontrar_maior()

# escolhi 10, 25 e 15 e o maior deles é 25.




