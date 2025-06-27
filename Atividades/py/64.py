# Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.

import random

def criar_lista_aleatoria():
    numeros = [random.randint(1, 100) for _ in range(10)]
    print("Lista de números aleatórios:")
    print(numeros)
    
    multiplos_de_3 = []
    for numero in numeros:
        if numero % 3 == 0:
            multiplos_de_3.append(numero)
    
    print("Números que são múltiplos de 3:")
    print(multiplos_de_3)

criar_lista_aleatoria()

#Lista de números aleatórios: [25, 100, 43, 39, 54, 45, 70, 11, 99, 23]