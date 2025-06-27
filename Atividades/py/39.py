#Crie um algoritmo que peça ao usuário para digitar uma senha e verifique se a senha é "1234".

def verificar_senha():
    senha_correta = "1234"
    senha_digitada = input("Digite a senha: ")
    
    if senha_digitada == senha_correta:
        print("Senha correta! Acesso concedido.")
    else:
        print("Senha incorreta. Acesso negado.")

verificar_senha()

#coloquei a senha 1234 e funcionou, depois coloquei 4321 e deu acesso negado.