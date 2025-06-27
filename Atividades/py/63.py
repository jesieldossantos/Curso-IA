# Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.

def solicitar_numeros():
    numeros = []
    
    for i in range(5):
        while True:
            try:
                numero = float(input(f"Digite o {i + 1}º número: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Por favor, digite um número válido.")
    
    soma = sum(numeros)
    print("Lista de números:")
    print(numeros)
    print(f"Soma dos números: {soma}")

solicitar_numeros()

#Lista de números:
#[4.0, 8.0, 17.0, 26.0, 7.0]
#Soma dos números: 62.0