# Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.

import time

def contagem_regressiva():
    try:
        numero = int(input("Digite um número: "))
        
        if numero <= 0:
            print("Por favor, digite um número positivo.")
        else:
            print(f"Contagem regressiva de {numero} a 1:")
            for i in range(numero, 0, -1):
                print(i)
                time.sleep(1)  # pausa por 1 segundo
            print("Fim da contagem regressiva!")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

contagem_regressiva()

# # #coloquei o número 5 e ele imprimiu a contagem regressiva de 5 a 1, com uma pausa de 1 segundo entre os números.