#  Faça um programa que pergunte ao usuário a idade e verifique se ele pode votar (idade maior ou igual a 16).

def verificar_voto():
    try:
        idade = int(input("Digite sua idade: "))
        if idade >= 16:
            print("Você pode votar!")
        else:
            print("Você não pode votar ainda. A idade mínima para votar é 16 anos.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    verificar_voto()

# escolhi 20 e pode votar.
#escolhi 15 e não pode votar.