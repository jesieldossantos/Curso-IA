# Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

print("Escolha um modo de transporte:")
print("1. Carro")
print("2. Bicicleta")
print("3. A pé")

escolha = input("Digite o número da sua escolha: ")

if escolha == "1":
    print("A velocidade média de um carro é de aproximadamente 60 km/h.")
elif escolha == "2":
    print("A velocidade média de uma bicicleta é de aproximadamente 15-25 km/h.")
elif escolha == "3":
    print("A velocidade média de uma pessoa a pé é de aproximadamente 5 km/h.")
else:
    print("Escolha inválida. Por favor, tente novamente.")

# 1= carro tem velocidade media de 60 km/h
# 2= bicicleta tem velocidade media de 15-25 km/h
# 3= a pe tem velocidade media de 5 km/h