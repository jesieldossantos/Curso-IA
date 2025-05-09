#Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.

def verificar_numeros():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        
        if num1 == num2 == num3:
            print("Os três números são iguais.")
        else:
            print("Os três números não são iguais.")
    except ValueError:
        print("Por favor, digite números válidos.")

verificar_numeros()

#escolhi 3 números iguais 5, 5 e 5 e funcionou, depois coloquei 3 números diferentes 3, 4, 8 e deu que não são iguais.