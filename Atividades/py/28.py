#  Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras

def verificar_palavra():
    palavra = input("Digite uma palavra: ").strip()
    if len(palavra) > 5:
        print(f"A palavra '{palavra}' tem mais de 5 letras")
    else:
        print(f"A palavra '{palavra}' tem 5 letras ou menos")

if __name__ == "__main__":
    verificar_palavra()

# escolhi casa e ela tem 5 letras ou menos
#escolhi jesiel e ela tem mais de 5 letras