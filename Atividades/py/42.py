# Escreva um algoritmo que solicite ao usuário 5 números inteiros e calcule a soma desses números.

def calcular_soma():
    try:
        numeros = []
        for i in range(5):
            numero = int(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)
        
        soma = sum(numeros)
        print(f"A soma dos números é: {soma}")
    except ValueError:
        print("Por favor, digite números inteiros válidos.")

calcular_soma()

#escolhi o número 5, 4, 3, 8, 9 e imprimiu a soma deles que é 29.