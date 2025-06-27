# Escreva um algoritmo que peça ao usuário o nome de uma fruta e verifique se a fruta é uma maçã.

fruta = input("Digite o nome de uma fruta: ").lower()

if fruta == "maçã":
    print("A fruta é uma maçã.")
else:
    print("A fruta não é uma maçã.")

frutas = ["maçã", "banana", "laranja"]

fruta = input("Digite o nome de uma fruta: ").lower()

if fruta in frutas:
    if fruta == "maçã":
        print("A fruta é uma maçã.")
    else:
        print(f"A fruta é uma {fruta}.")
else:
    print("Fruta não encontrada.")

# escolhi pêra que não é maçã
# escolhi maçã que é maçã
# escolhi banana que não é maçã