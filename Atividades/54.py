#Crie um algoritmo que solicite ao usuário um número e continue pedindo outro número até que um número negativo seja inserido.

def solicitar_numeros():
    try:
        soma = 0
        count = 0
        while True:
            numero = float(input("Digite um número (número negativo para parar): "))
            if numero < 0:
                print("Número negativo inserido. Parando...")
                if count > 0:
                    print(f"Soma dos números: {soma}")
                    print(f"Média dos números: {soma / count}")
                break
            else:
                soma += numero
                count += 1
                print(f"Você digitou: {numero}")
    except ValueError:
        print("Por favor, digite um número válido.")

solicitar_numeros()

#escolhi o numero 5 e 5 e ele imprimiu a soma deles, que é 10. e -7 para parar.
