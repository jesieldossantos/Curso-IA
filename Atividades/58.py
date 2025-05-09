#Desenvolva um algoritmo que solicite ao usuário uma palavra e continue pedindo outra palavra até que ele digite "sair".

def solicitar_palavras():
    while True:
        palavra = input("Digite uma palavra (ou 'sair' para parar): ").lower()
        if palavra == "sair":
            print("Programa encerrado.")
            break
        else:
            print(f"Você digitou: {palavra}")

solicitar_palavras()

# #coloquei a palavra "amem" e ele imprimiu "Você digitou: amem".
