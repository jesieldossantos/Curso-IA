#Escreva um algoritmo que peça ao usuário um número de 1 a 5 e verifique se ele é igual a 3.

def verificar_numero():
    while True:
        try:
            numero = int(input("Digite um número de 1 a 5: "))
            if 1 <= numero <= 5:
                if numero == 3:
                    print("O número é igual a 3!")
                else:
                    print("O número não é igual a 3.")
                break
            else:
                print("Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Por favor, digite um número válido.")

verificar_numero()

#escolhi 3 e é igual a 3.
#escolhi 4 e não é igual a 3.