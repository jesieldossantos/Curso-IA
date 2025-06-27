#Escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o nome, 3, excluir, 4-listar todos os cadastrados, ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.

class GerenciadorDeNomes:
    def __init__(self):
        self.nomes = []

def cadastrar_nome(self):
    nome = input("Digite o nome a ser cadastrado: ")
    self.nomes.append(nome)
    return f"Nome '{nome}' cadastrado com sucesso!"

def atualizar_nome(self):
    if not self.nomes:
        return "Não há nomes cadastrados para atualizar."
    
    print("Nomes cadastrados:")
    for i, nome in enumerate(self.nomes):
        print(f"{i + 1}. {nome}")
    
    try:
        indice = int(input("Digite o número do nome a ser atualizado: ")) - 1
        if indice < 0 or indice >= len(self.nomes):
            return "Índice inválido."
    except ValueError:
        return "Entrada inválida. Por favor, insira um número."
def excluir_nome(self):
    if not self.nomes:
        return "Não há nomes cadastrados para excluir."
    
    print("Nomes cadastrados:")
    for i, nome in enumerate(self.nomes):
        print(f"{i + 1}. {nome}")
    
    try:
        indice = int(input("Digite o número do nome a ser excluído: ")) - 1
        if indice < 0 or indice >= len(self.nomes):
            return "Índice inválido."
        
        nome_excluido = self.nomes.pop(indice)
        return f"Nome '{nome_excluido}' excluído com sucesso!"
    except ValueError:
        return "Índice inválido."

def listar_nomes(self):
    if not self.nomes:
        return "Não há nomes cadastrados."
    
    return "Nomes cadastrados:\n" + "\n".join(self.nomes)

def main():
    gerenciador = GerenciadorDeNomes()
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar nome")
        print("2. Atualizar nome")
        print("3. Excluir nome")
        print("4. Listar nomes")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            resultado = gerenciador.cadastrar_nome()
        elif opcao == "2":
            resultado = gerenciador.atualizar_nome()
        elif opcao == "3":
            resultado = gerenciador.excluir_nome()
        elif opcao == "4":
            resultado = gerenciador.listar_nomes()
        else:
            print("Operação encerrada.")
            break
        
        print(resultado)
        resposta = input("Deseja realizar outra operação? (s/n): ")
    if resposta.lower() != "s":
        print("Operação encerrada.")

