#

precos = {
    "gasolina": 5.58,
    "etanol": 4.27,
    "diesel": 4.05
}

print("Escolha um tipo de combustível:")
for combustivel in precos.keys():
    print(f"- {combustivel.capitalize()}")

escolha = input("Digite o tipo de combustível: ").lower()

if escolha in precos:
    print(f"O preço do {escolha} é R$ {precos[escolha]:.2f} por litro.")
else:
    print("Combustível inválido. Por favor, tente novamente.")

precos = {
    "gasolina": 5.50,
    "etanol": 4.20,
    "diesel": 4.50
}

while True:
    print("1. Ver preço")
    print("2. Atualizar preço")
    print("3. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        print("Escolha um tipo de combustível:")
        for combustivel in precos.keys():
            print(f"- {combustivel.capitalize()}")

        combustivel_escolhido = input("Digite o tipo de combustível: ").lower()
        if combustivel_escolhido in precos:
            print(f"O preço do {combustivel_escolhido} é R$ {precos[combustivel_escolhido]:.2f} por litro.")
        else:
            print("Combustível inválido. Por favor, tente novamente.")
    elif escolha == "2":
        combustivel = input("Digite o tipo de combustível: ").lower()
        preco = float(input("Digite o novo preço: "))

        if combustivel in precos:
            precos[combustivel] = preco
            print(f"Preço do {combustivel} atualizado para R$ {preco:.2f}.")
        else:
            print("Combustível inválido. Por favor, tente novamente.")
    elif escolha == "3":
        break
    else:
        print("Escolha inválida. Por favor, tente novamente.")

