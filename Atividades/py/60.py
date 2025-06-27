#Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.

def encontrar_divisores():
    try:
        numero = int(input("Digite um número: "))
        
        if numero == 0:
            print("O número 0 tem todos os números como divisores, mas isso não é muito útil.")
        else:
            divisores = [i for i in range(1, abs(numero) + 1) if numero % i == 0]
            print(f"Os divisores de {numero} são: {divisores}")
    except ValueError:
        print("Por favor, digite um número válido.")

encontrar_divisores()

# coloquei o numero 6 e ele imprimiu "Os divisores de 6 são: [1, 2, 3, 6]"