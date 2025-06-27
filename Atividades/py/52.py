# Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.

def solicitar_senha():
    senha_correta = "1234"
    while True:
        senha = input("Digite a senha: ")
        if senha == senha_correta:
            print("Senha correta! Acesso concedido.")
            break
        else:
            print("Senha incorreta. Tente novamente.")

solicitar_senha()

# #coloquei a senha "1234" e ele imprimiu "Senha correta! Acesso concedido."
# #coloquei a senha "4567" e ele imprimiu "Senha incorreta. Tente novamente."
