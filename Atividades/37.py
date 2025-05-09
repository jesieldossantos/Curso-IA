#Desenvolva um algoritmo que peça ao usuário para digitar um número e verifique se ele é múltiplo de 2 ou de 5.

def verificar_multiplo():
    try:
        numero = int(input("Digite um número: "))
        multiplos = []
        if numero % 2 == 0:
            multiplos.append("2")
        if numero % 5 == 0:
            multiplos.append("5")
        if multiplos:
            print(f"O número {numero} é múltiplo de {', '.join(multiplos)}.")
        else:
            print(f"O número {numero} não é múltiplo de 2 nem de 5.")
    except ValueError:
        print("Por favor, digite um número válido.")

verificar_multiplo()

#escolhi 40 e é múltiplo de 2 e 5.