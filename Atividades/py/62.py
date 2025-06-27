# Escreva um programa que solicite ao usuário para inserir 3 nomes e armazene-os em uma lista. Em seguida, imprima a lista completa.

def solicitar_nomes():
    nomes = []
    
    for i in range(3):
        nome = input(f"Digite o {i + 1}º nome: ")
        nomes.append(nome)
    
    print("Lista de nomes:")
    print(nomes)

solicitar_nomes()

# coloquei joao, dilma e jesiel e ele imprimiu "Lista de nomes: ['joao', 'dilma', 'jesiel']"