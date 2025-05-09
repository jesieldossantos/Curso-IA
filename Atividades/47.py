# Crie um programa que peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

def exibir_tabuada():
    try:
        numero = int(input("Digite um número: "))
        
        print(f"Tabuada do {numero}:")
        print("\n".join(f"{numero} x {i} = {numero * i}" for i in range(1, 11)))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

exibir_tabuada()

#escreva um número: 5
#Tabuada do 5:
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35
#5 x 8 = 40
#5 x 9 = 45
#5 x 10 = 50