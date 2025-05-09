# Escreva um programa que solicite ao usuário para digitar seu nome e, em seguida, exiba uma mensagem de boas-vindas personalizada.

nome = input("Digite seu nome: ")

print(f"Bem-vindo(a), {nome}!")

nome = input("Digite seu nome: ")

if nome.strip() == "":
    print("Por favor, digite seu nome.")
else:
    print(f"Bem-vindo(a) ao meu mundo, {nome}!")

# karol
# Bem vindo(a) ao meu mundo karol!