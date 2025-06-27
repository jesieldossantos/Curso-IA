#. Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0).

def calcular_soma():
    try:
        soma = 0
        while True:
            numero = float(input("Digite um número (0 para parar): "))
            if numero == 0:
                break
            soma += numero
        
        print(f"A soma dos números inseridos é: {soma}")
    except ValueError:
        print("Por favor, digite números válidos.")

calcular_soma()

# # #coloquei os números 1, 2, 3 e 0, e ele imprimiu a soma deles, que é 6.


