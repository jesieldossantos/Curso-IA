# Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes.

def exibir_mensagem():
    try:
        mensagem = input("Digite a mensagem que você deseja exibir: ")
        vezes = int(input("Quantas vezes você deseja exibir a mensagem? "))
        
        if vezes <= 0:
            print("Por favor, digite um número positivo.")
        else:
            for _ in range(vezes):
                print(mensagem)
    except ValueError:
        print("Por favor, digite um número válido.")

exibir_mensagem()

# #coloquei a mensagem "seja bem vindo!" e o número 3, e ele imprimiu a mensagem 3 vezes.