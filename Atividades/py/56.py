#  Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.

def exibir_mensagem():
    try:
        mensagem = input("Digite a mensagem que você quer exibir: ")
        vezes = int(input("Quantas vezes você quer exibir a mensagem? "))
        
        contador = 0
        while contador < vezes:
            print(mensagem)
            contador += 1
    except ValueError:
        print("Por favor, digite um número válido.")

exibir_mensagem()

# # #coloquei a mensagem "oi, tudo bem?" e o número 4, e ele imprimiu a mensagem 4 vezes.