# 6. Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

num1 = float(input("Digite o rimeiro número: "))
num2 = float(input("Digite o segundo número: "))

def calculadora():

    print('1 - soma')
    print('2 - subtraçao')
    print('3 - Multiplicação')
    print('4 - Divisão')

    operacao = int(input('Escolha a operação desejada'))

    match operacao:
        case 1:
            print('A soma é: ' + str(num1 + num2))
            print(f'A soma é: {num1 + num2}')
        case 2:
            print('A subtração é: ' + str(num1 - num2))
        case 3:
            print('A multiplicação é: ' + str(num1 * num2))
        case 4:
            print('A divisão é: ' + str(num1 / num2))
        case _:
            print('operacao')
            return