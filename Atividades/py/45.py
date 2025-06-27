#Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.

def exibir_maior():
    try:
        numeros = []
        for i in range(5):
            numero = float(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)
        
        maior = max(numeros)
        print(f"O maior número inserido é: {maior}")
    except ValueError:
        print("Por favor, digite números válidos.")

exibir_maior()

#Digite o 1º número: 5
#Digite o 2º número: 4
#Digite o 3º número: 8
#Digite o 4º número: 7
#Digite o 5º número: 9
#O maior número inserido é: 9