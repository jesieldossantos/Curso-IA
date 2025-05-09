
def verificar_palavra():
    palavra = input("Digite uma palavra: ").strip().lower()
    if palavra == "python":
        print("A palavra é Python")
    else:
        print(f"A palavra '{palavra}' não é Python")

if __name__ == "__main__":
    verificar_palavra()

# escolh agua que não é python
# escolho python que é python