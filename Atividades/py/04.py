# 4. Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

cor = input('selecione uma das cores vermelho, verde, azul: ')

cor = cor.lower()

if (cor == 'vermelho') or (cor == 'azul') or (cor == 'verde'):
    print(f'a cor escolhida foi {cor} ')
else:
    print('cor invalida')