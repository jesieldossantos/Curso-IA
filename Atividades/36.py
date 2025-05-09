#Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente

def exibir_mes():
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    
    try:
        numero = int(input("Digite um número de 1 a 12: "))
        if 1 <= numero <= 12:
            print(f"O mês correspondente ao número {numero} é {meses[numero]}.")
        else:
            print("Por favor, digite um número entre 1 e 12.")
    except ValueError:
        print("Por favor, digite um número válido.")

exibir_mes()

#escolhi 12 e o mês correspondente é dezembro.