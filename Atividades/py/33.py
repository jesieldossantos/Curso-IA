# Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%.

def calcular_desconto():
    try:
        valor = float(input("Digite o valor do produto: R$ "))
        desconto = valor * 0.10
        valor_com_desconto = valor - desconto
        print(f"Valor original: R$ {valor:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
    except ValueError:
        print("Por favor, digite um valor válido.")

calcular_desconto()

# escolhi 4.50 e o desconto foi de 0.45. assim o valor total ficou 4.05.