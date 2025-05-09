import os
os.system('cls')


def soma(numero1, numero2):
    soma = numero1 + numero2
    return soma


def subtracao(numero1, numero2):
    subtracao = numero1 - numero2
    return subtracao


def multiplicacao(numero1, numero2):
    multiplicacao = numero1 * numero2
    return multiplicacao

def divisao(numero1, numero2):
    divisao = numero1 * numero2
    return divisao



numero1 = int(input(' informe o primeiro numero '))
numero2 = int(input(' informe o segundo numero '))

print('1 - soma')
print('2 - subtracao')
print('3 - multiplicacao')
print('4 - divisao')

operacao =int(input('selecione uma das operacoes: '))

match operacao:
    case 1:
        print(f'a soma é: {soma(numero1, numero2)}')
    case 2:
        print(f'a subtracao é: {subtracao(numero1, numero2)}')
    case 3:
        print(f'a multiplicacao é: {multiplicacao(numero1, numero2)}')
    case 4:
        print(f'a divisao é: {divisao(numero1, numero2)}')