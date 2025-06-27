

mes = int(input("Digite um mês do ano (1 a 12): "))

if mes in [12, 1, 2]:
    print("A estação do ano correspondente é o Verão.")
elif mes in [3, 4, 5]:
    print("A estação do ano correspondente é o Outono.")
elif mes in [6, 7, 8]:
    print("A estação do ano correspondente é o Inverno.")
elif mes in [9, 10, 11]:
    print("A estação do ano correspondente é a Primavera.")
else:
    print("Mês inválido. Por favor, digite um número entre 1 e 12.")

# 4= primavera
# 5= outono
# 10= inverno
# 01= verao 