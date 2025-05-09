#Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. Continue pedindo até que ele adivinhe o número corretamente.

import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar um número entre 1 e 10.")
    
    while True:
        try:
            chute = int(input("Digite seu chute: "))
            tentativas += 1
            
            if chute < 1 or chute > 10:
                print("Por favor, digite um número entre 1 e 10.")
            elif chute < numero_secreto:
                print("Seu chute é muito baixo. Tente novamente!")
            elif chute > numero_secreto:
                print("Seu chute é muito alto. Tente novamente!")
            else:
                print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, digite um número válido.")

adivinhar_numero()

#Parabéns! Você adivinhou o número secreto 10 em 6 tentativas.