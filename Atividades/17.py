

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2

    print(f"Soma: {num1} + {num2} = {soma}")
    print(f"Subtração: {num1} - {num2} = {subtracao}")
    print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")

    if num2 != 0:
        divisao = num1 / num2
        print(f"Divisão: {num1} / {num2} = {divisao}")
    else:
        print("Não é possível realizar a divisão por zero.")
except ValueError:
    print("Por favor, insira um número válido.")

# escolhi o numero 20 e 2.
# na soma deu 22
# na subtracao deu 18
# na multiplicacao deu 40
# na divisao deu 10