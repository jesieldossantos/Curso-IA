#Desenvolva um programa que peça ao usuário para inserir um número maior que 100. Se o número for menor ou igual a 100, continue pedindo até que um número maior que 100 seja inserido.

def solicitar_numero():
    try:
        while True:
            numero = float(input("Digite um número maior que 100: "))
            if numero > 100:
                print(f"Número válido: {numero}")
                break
            else:
                print("Número inválido. Por favor, digite um número maior que 100.")
    except ValueError:
        print("Por favor, digite um número válido.")

solicitar_numero()

# #coloquei o número 50 e ele pediu para colocar um número maior que 100, depois coloquei o número 104 e ele imprimiu o número válido.
