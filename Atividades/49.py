#Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10.

def contar_maiores_que_10():
    try:
        numeros = []
        for i in range(7):
            numero = float(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)
        
        maiores_que_10 = sum(1 for numero in numeros if numero > 10)
        print(f"Quantidade de números maiores que 10: {maiores_que_10}")
    except ValueError:
        print("Por favor, digite números válidos.")

contar_maiores_que_10()

# Example input/output:
# Digite o 1º número: 2
# Digite o 2º número: 4
# Digite o 3º número: 6
# Digite o 4º número: 8
# Digite o 5º número: 10
# Digite o 6º número: 12
# Digite o 7º número: 14