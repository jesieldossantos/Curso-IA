#  Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

estado_civil = input("Digite o seu estado civil (solteiro, casado, divorciado, viúvo): ").lower()

if estado_civil == "solteiro":
    print("Você é solteiro(a). Que liberdade!")
elif estado_civil == "casado":
    print("Você é casado(a). Parabéns pelo compromisso!")
elif estado_civil == "divorciado":
    print("Você é divorciado(a). Nova jornada à frente!")
elif estado_civil == "viúvo":
    print("Você é viúvo(a). Meus sentimentos.")
else:
    print("Estado civil inválido. Por favor, tente novamente.")

# Você e solteiro(a). Que liberdade!
# Você e casado(a). Parabéns pelo compromisso!
# Você e divorciado(a). Nova jornada à frente!
# Você e viúvo(a). Meus sentimentos.
