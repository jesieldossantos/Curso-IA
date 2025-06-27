# Faça um programa que peça ao usuário três números e verifique se todos são positivos.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > 0 and num2 > 0 and num3 > 0:
    print("Todos os números são positivos.")
else:
    print("Nem todos os números são positivos.")
# Removed misplaced except block

def verificar_positivos(*numeros):
    return all(numero > 0 for numero in numeros)

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    if verificar_positivos(num1, num2, num3):
        print("Todos os números são positivos.")
    else:
        print("Nem todos os números são positivos.")
except ValueError:
    print("Entrada inválida. Por favor, digite números.")

# ex1 = 30, 45, 17 # todos são positivos
# ex2 = 30, -45, 17 # nem todos são positivos
# ex3 = 0, 45, 17 # nem todos são positivos