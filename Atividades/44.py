# Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.

def exibir_pares():
    try:
        pares = [int(input(f"Digite o {i + 1}º número: ")) for i in range(10) if int(input(f"Digite o {i + 1}º número: ")) % 2 == 0]
        print("Números pares:")
        print(pares)
    except ValueError:
        print("Por favor, digite números inteiros válidos.")

exibir_pares()

#Digite o 1º número: 4
# Digite o 1º número: 5
#Digite o 2º número: 7
#Digite o 3º número: 8
#Digite o 3º número: 9
#Digite o 4º número: 10
#Digite o 4º número: 12
#Digite o 5º número: 11
#Digite o 6º número: 21
#Digite o 7º número: 23
#Digite o 8º número: 25
#Digite o 9º número: 30
#Digite o 9º número: 24
#Digite o 10º número: 87
#Números pares:
#[5, 7, 9, 12, 24]