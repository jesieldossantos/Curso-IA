#Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo.

def solicitar_numeros():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if num1 > num2:
                print(f"{num1} é maior que {num2}. Condição atendida!")
                break
            else:
                print(f"{num1} não é maior que {num2}. Tente novamente!")
                print(f"Lembre-se de que {num1} precisa ser maior que {num2}.")
        except ValueError:
            print("Por favor, digite números válidos.")

solicitar_numeros()

# coloquei o numero 4 e 9 e ele imprimiu "4 não é maior que 9. Tente novamente!"
# coloquei o numero 10 e 5 e ele imprimiu "10 é maior que 5. Condição atendida!"

