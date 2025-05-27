import requests


def buscar_endereco(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        endereco = f"{dados['logradouro']}, {dados['bairro']}, {dados['localidade']} - {dados['uf']}"
        print(endereco)

