#  Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três")

# if (numero == 1):
#     print('o numero digitado foi:' )
#     print('um')
# elif (numero == 2):
#     print('o numero digitado foi:' )
#     print('dois')
# elif (numero == 3):
#     print('o numero digitado foi:' )
#     print('tres')
# else:
#     print('o numero nao esta entre 1 e 3' )

numero = int(input("Informe um número de 1 a 3: "))

match numero:
    case 1:
        print('o numero digitado foi um' )
    case 2:
        print('o numero digitado foi dois' )
    case 3: 
        print('o numero digitado foi tres' )
    case _ :
        print(' o numero nao esta ente 1 e 3' )

