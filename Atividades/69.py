# Crie no algoritmo 67 as seguintes funcionalidades:
# Informe ao usuário em caso de empate.
# Crie uma forma de não permitir que um jogador jogue no mesmo lugar que já tenha uma jogada realizada.
# Atualmente o jogo encerra com o vencedor, ele agora também deve encerrar em caso de empate.
# Ao finalizar o jogo deve ser informado ao usuário uma mensagem solicitando uma nova partida, o sistema de reiniciar o jogo em caso de sim, e encerrar o programa em caso de não.
# Refatore a funcionalidade que verifica a vitória.
# Pense em uma forma de simplificar o código corrigido.

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [" "] * 9
        self.jogador_atual = "X"

    def imprimir_tabuleiro(self):
        print(f" {self.tabuleiro[0]} | {self.tabuleiro[1]} | {self.tabuleiro[2]} ")
        print("---+---+---")
        print(f" {self.tabuleiro[3]} | {self.tabuleiro[4]} | {self.tabuleiro[5]} ")
        print("---+---+---")
        print(f" {self.tabuleiro[6]} | {self.tabuleiro[7]} | {self.tabuleiro[8]} ")

def verificar_vencedor(self):
    linhas = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    colunas = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    diagonais = [(0, 4, 8), (2, 4, 6)]
    combinacoes_vencedoras = linhas + colunas + diagonais

    for combinacao in combinacoes_vencedoras:
        if self.tabuleiro[combinacao[0]] == self.tabuleiro[combinacao[1]] == self.tabuleiro[combinacao[2]] != " ":
            return self.tabuleiro[combinacao[0]]

    if " " not in self.tabuleiro:
        return "Empate"

    return False

def jogar(self):
    while True:
        self.imprimir_tabuleiro()
        while True:
            try:
                jogada = int(input(f"Jogador {self.jogador_atual}, digite a posição da sua jogada (1-9): "))
                if jogada < 1 or jogada > 9:
                    print("Posição inválida. Digite um número entre 1 e 9.")
                elif self.tabuleiro[jogada - 1] != " ":
                    print("Posição ocupada. Tente novamente.")
                else:
                    self.tabuleiro[jogada - 1] = self.jogador_atual
                    break
            except ValueError:
                print("Entrada inválida. Digite um número.")

        resultado = self.verificar_vencedor()
        if resultado:
            self.imprimir_tabuleiro()
            if resultado == "Empate":
                print("Empate!")
            else:
                print(f"Jogador {resultado} venceu!")
            return  # Use return to exit the method instead of break

        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() == "s":
            self.tabuleiro = [" "] * 9
            self.jogador_atual = "X"
            self.jogar()
        else:
            print("Obrigado por jogar!")

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()

