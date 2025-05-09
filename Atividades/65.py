#Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.

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
    
    print("Lista de números:")
    print(numeros)
    
    maior_numero = max(numeros)
    menor_numero = min(numeros)
    
    print(f"Maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")

solicitar_numeros()

#Lista de números: [8.0, 50.0, 47.0, 63.0, 82.0] Maior número: 82.0 Menor número: 8.0