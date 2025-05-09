#Crie um programa que peça ao usuário para inserir um número e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente.

def exibir_decrescente():
    try:
        numero = int(input("Digite um número: "))
        
        if numero > 0:
            print(f"Números de {numero} a 1:")
            print(*range(numero, 0, -1), sep='\n')
        else:
            print("Por favor, digite um número positivo.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

exibir_decrescente()

# digitei o numero 6
# Números de 6 a 1:
# 6
# 5
# 4
# 3
# 2
# 1
