# Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

if soma > 100:
    print(f"A soma dos números é {soma}, que é maior que 100.")
elif soma == 100:
    print(f"A soma dos números é {soma}, que é igual a 100.")
else:
    print(f"A soma dos números é {soma}, que é menor que 100.")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

if soma > 100:
    print(f"A soma dos números é {soma}, que é maior que 100.")
elif soma == 100:
    print(f"A soma dos números é {soma}, que é igual a 100.")
else:
    print(f"A soma dos números é {soma}, que é menor que 100.")

# escolhi 30 e 45 que da 75 e não é maior que 100
# escolhi 33 e 68 que da 101 e é maior que 100
# escolhi 50 e 50 que da 100 e é igual a 100