# 5. Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print('Ambos os números são pares')
else:
    print('um ou ambos os números não são pares')
