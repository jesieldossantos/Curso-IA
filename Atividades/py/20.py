
def converter_celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    try:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = converter_celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    main()

def converter_celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def converter_fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("1. Converter Celsius para Fahrenheit")
        print("2. Converter Fahrenheit para Celsius")
        print("3. Sair")
        
        escolha = input("Digite sua escolha: ")
        
        if escolha == "1":
            try:
                celsius = float(input("Digite a temperatura em graus Celsius: "))
                fahrenheit = converter_celsius_para_fahrenheit(celsius)
                print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        elif escolha == "2":
            try:
                fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
                celsius = converter_fahrenheit_para_celsius(fahrenheit)
                print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")


# 42 graus celsius = 107.6 graus fahrenheit