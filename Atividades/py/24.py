#  Desenvolva um algoritmo que pergunte ao usuário o nome de uma cidade e verifique se é a capital do Brasil.

def verificar_capital():
    capital = "brasília"
    while True:
        cidade = input("Digite o nome de uma cidade (ou 'sair' para parar): ").strip().lower()
        if cidade == 'sair':
            break
        if cidade == capital:
            print(f"{cidade.capitalize()} é a capital do Brasil")
        else:
            print(f"{cidade.capitalize()} não é a capital do Brasil")

if __name__ == "__main__":
    verificar_capital()

# ceilandia que não é a capital do Brasil
# brasília que é a capital do Brasil