# Crie um programa que peça ao usuário um número inteiro positivo e exiba todos os números de 1 até o número informado.

def exibir_numeros():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        
        if numero <= 0:
            print("Por favor, digite um número inteiro positivo.")
        else:
            print(f"Números de 1 a {numero}:")
            for i in range(1, numero + 1):
                print(i)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

exibir_numeros()

# #coloquei o número 5 e ele imprimiu os números de 1 a 5, depois coloquei -3 e deu que não era positivo.