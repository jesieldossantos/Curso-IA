# Escreva um programa que peça ao usuário um número de 0 a 20 e verifique se ele está entre 10 e 15.

def verificar_intervalo():
    while True:
        try:
            numero = input("Digite um número de 0 a 20 (ou 'sair' para parar): ")
            if numero.lower() == 'sair':
                break
            numero = int(numero)
            if 0 <= numero <= 20:
                if 10 <= numero <= 15:
                    print(f"O número {numero} está entre 10 e 15")
                else:
                    print(f"O número {numero} não está entre 10 e 15")
            else:
                print("O número deve estar entre 0 e 20")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    verificar_intervalo()

# escolhi 15 que esta entre 10 e 15.
# escolhi 17 que não esta entre 10 e 15.