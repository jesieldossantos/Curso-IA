# desenvolva um jogo da velha em python que funcione no terminal

def imprimir_tabuleiro(tabuleiro):
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")

def verificar_vencedor(tabuleiro):
    combinacoes_vencedoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combinacao in combinacoes_vencedoras:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] != " ":
            return tabuleiro[combinacao[0]]
    if " " not in tabuleiro:
        return "Empate"
    return False

def jogo_da_velha():
    tabuleiro = [" "] * 9
    jogador_atual = "X"
    while True:
        imprimir_tabuleiro(tabuleiro)
        jogada = input(f"Jogador {jogador_atual}, digite a posição (1-9): ")
        if tabuleiro[int(jogada) - 1] != " ":
            print("Posição ocupada. Tente novamente.")
            continue
        tabuleiro[int(jogada) - 1] = jogador_atual
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            imprimir_tabuleiro(tabuleiro)
            if vencedor == "Empate":
                print("Empate!")
            else:
                print(f"Jogador {vencedor} venceu!")
            break
        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogo_da_velha()
