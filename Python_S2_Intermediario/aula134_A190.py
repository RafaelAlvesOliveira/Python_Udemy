import json

pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Alves',
    'enderecos': [
        {'rua': 'Planta da sorte', 'numero': 81},
        {'rua': 'Leonor Souza', 'numero': 55},
    ],
    'altura': 1.75,
    'numeros-preferidos': [2, 4, 6, 8, 18],
    'dev': True,
    'nada': None,
}

with open('aula134_A190.json', 'w', encoding='utf-8') as arquivo:
    # Sempre colocar encoding='utf-8' para não gerar problemas com
    # acentuação.
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)
    # dump é para fazer o envio do arquivo para fora da pasta ou do arquivo
    # de origem.  O comando ensure_ascii faz com que o arquivo seja
    # carregado com a acentuação e outros caracteres especiais.
    # Indent serve para formatar o arquivo json, semelhante ao dicionário.

with open('aula134_A190.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
