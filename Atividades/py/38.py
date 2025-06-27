# Escreva um programa que peça ao usuário para digitar sua altura em metros e verifique se ela é maior que 1.75.

def verificar_altura():
    try:
        altura = float(input("Digite sua altura em metros: "))
        if altura > 1.75:
            print(f"Sua altura ({altura:.2f}m) é maior que 1.75m.")
        elif altura == 1.75:
            print(f"Sua altura ({altura:.2f}m) é igual a 1.75m.")
        else:
            print(f"Sua altura ({altura:.2f}m) é menor que 1.75m.")
    except ValueError:
        print("Por favor, digite uma altura válida.")

verificar_altura()

#Sua altura (1.68m) é menor que 1.75m.