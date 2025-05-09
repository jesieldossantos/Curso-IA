#Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.

def verificar_multiplicacao():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        produto = num1 * num2
        if produto == 20:
            print(f"A multiplicação de {num1} e {num2} é igual a 20.")
        else:
            print(f"A multiplicação de {num1} e {num2} é igual a {produto}, não 20.")
    except ValueError:
        print("Por favor, digite números válidos.")

verificar_multiplicacao()

#escolhi 4 e 58 e a multiplicação é igual a 32.
#escolhi 5 e 4 e a multiplicação é igual a 20.
