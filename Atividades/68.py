


import uuid
from datetime import datetime

class Aluno:
    def __init__(self, nome, email, data_nascimento):
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento
        self.matricula = str(uuid.uuid4().int)[:10]

    def __str__(self):
        return f"Nome: {self.nome}\nE-mail: {self.email}\nData de Nascimento: {self.data_nascimento}\nMatricula: {self.matricula}"

    def atualizar_nome(self, novo_nome):
        self.nome = novo_nome

    def atualizar_email(self, novo_email):
        self.email = novo_email

    def atualizar_data_nascimento(self, nova_data_nascimento):
        self.data_nascimento = nova_data_nascimento


# (Line removed as it is unnecessary and causes a syntax error)

# Removed redundant import of Aluno

class GerenciadorDeAlunos:
    def __init__(self):
        self.alunos = []

    def cadastrar_aluno(self):
        nome = input("Digite o nome do aluno: ")
        email = input("Digite o e-mail do aluno: ")
        data_nascimento = input("Digite a data de nascimento do aluno (dd/mm/aaaa): ")
        
        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")
        except ValueError:
            print("Data de nascimento inválida.")
            return
        
        aluno = Aluno(nome, email, data_nascimento)
        self.alunos.append(aluno)
        print(f"Aluno '{nome}' cadastrado com sucesso! Matricula: {aluno.matricula}")

    def atualizar_aluno(self):
        matricula = input("Digite a matricula do aluno: ")
        aluno = self.encontrar_aluno_por_matricula(matricula)
        
        if aluno is None:
            print("Aluno não encontrado.")
            return
        
        print("1. Atualizar nome")
        print("2. Atualizar e-mail")
        print("3. Atualizar data de nascimento")
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            novo_nome = input("Digite o novo nome: ")
            aluno.atualizar_nome(novo_nome)
            print(f"Nome do aluno '{aluno.nome}' atualizado com sucesso!")
        elif opcao == "2":
            novo_email = input("Digite o novo e-mail: ")
            aluno.atualizar_email(novo_email)
            print(f"E-mail do aluno '{aluno.nome}' atualizado com sucesso!")
        elif opcao == "3":
            nova_data_nascimento = input("Digite a nova data de nascimento (dd/mm/aaaa): ")
            try:
                datetime.strptime(nova_data_nascimento, "%d/%m/%Y")
            except ValueError:
                print("Data de nascimento inválida.")
                return
            aluno.atualizar_data_nascimento(nova_data_nascimento)
            print(f"Data de nascimento do aluno '{aluno.nome}' atualizada com sucesso!")
        else:
            print("Opção inválida.")

    def excluir_aluno(self):
        matricula = input("Digite a matricula do aluno: ")
        aluno = self.encontrar_aluno_por_matricula(matricula)
        
        if aluno is None:
            print("Aluno não encontrado.")
            return
        
        self.alunos.remove(aluno)
        print(f"Aluno '{aluno.nome}' excluído com sucesso!")

    def listar_alunos(self):
        if not self.alunos:
            print("Não há alunos cadastrados.")
            return
        
        for aluno in self.alunos:
            print(aluno)
            print("------------------------")

    def encontrar_aluno_por_matricula(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def mostrar_aluno(self):
        matricula = input("Digite a matricula do aluno: ")
        aluno = self.encontrar_aluno_por_matricula(matricula)
        
        if aluno is None:
            print("Aluno não encontrado.")
            return
        
        print(aluno)


# Removed unnecessary import as GerenciadorDeAlunos is defined in this file

def main():
    gerenciador = GerenciadorDeAlunos()
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar aluno")
        print("2. Atualizar aluno")
        print("3. Excluir aluno")
        print("4. Listar alunos")
        print("5. Mostrar aluno")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            gerenciador.cadastrar_aluno()
        if opcao == "2":
            gerenciador.atualizar_aluno()

if __name__ == "__main__":
    main()
