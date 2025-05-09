# Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.

def calcular_media():
    try:
        numeros = []
        for i in range(10):
            numero = float(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)
        
        media = sum(numeros) / len(numeros)
        print(f"A média dos números inseridos é: {media:.2f}")
    except ValueError:
        print("Por favor, digite números válidos.")

calcular_media()

#Digite o 1º número: 6
#Digite o 2º número: 8
#Digite o 3º número: 4
# Digite o 4º número: 2
# Digite o 5º número: 10
# Digite o 6º número: 12
# Digite o 7º número: 80
# Digite o 8º número: 60
# Digite o 9º número: 84
# Digite o 10º número: 64
# A média dos números inseridos é: 33.00