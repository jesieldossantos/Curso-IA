# cor = input("informe a cor ")

# if (cor == 'preto'):
#     print('voce e cotista')

# elif ('cor == pardo'):
#     print('voce  tambem e cotista')
# else:
#      print('voce nao e cotista'

# idade = int(input("Qual a sua idade? "))
# altura= float(input("Qual a sua altura? "))

# if (idade >= 18) and (altura > 1.50):
#     print('Voce pode ir no brinquedo')
# else:
#     print('voce nao pode ir no brinquedo')


print('selecione sua refeição')
print(' 1 - hamburguer')
print(' 2 - pizza ')
print(' 3 - bolo ')
print(' 4 - maçã ')

escolha = int(input('Qual a opçap desejada '))

match escolha:
       
    case 1 :
         print('hamburguer, seja mais saudavel')
    case 2 :
         print('Pizza, seja mais saudavel')
    case 3 :
         print('Bolo, boa escolha')
    case 4 :
         print('maçã, ouse mais')
    case _ :
         print('escolha invalida')
         print('programa encerrado com sucesso')
