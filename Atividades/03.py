# 3. Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

dia = int(input("Digite o número do dia da semana (1 a 7): "))

def dia_da_semana():
    dias = {
        1: "domingo",
        2: "segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado",
    }

match dia:
    case 1:
        print('domingo')
    case 2:
        print('segunda-feira')
    case 3:
        print('terça-feira')
    case 4:
        print('quarta-feira')
    case 5:
        print('quinta-feira')
    case 6:
        print('sexta-feira')
    case 7:
        print('sábado')
    case _:
        print('dia invalido.')

