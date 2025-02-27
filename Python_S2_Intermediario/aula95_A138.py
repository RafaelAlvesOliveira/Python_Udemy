# list comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*novos_produtos, sep='\n')
# pprint.pprint(novos_produtos, sort_dicts=False, width=40)
# p(novos_produtos)

# lista = [n for n in range(10)]
# lista = [n for n in range(10) if n < 5]
# print(lista)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
    # if produto['preco'] > 10
]

p(novos_produtos)

# os itens a esquerda do 'for' são para mapeamento
# e os que estão a direita são filtros

# Mapeamento é pegar um dado e transformar ou não
# um determinado dado, e se for necessário
# jogar o mesmo em outra lista, e as duas listas
# tem o mesmo tamanho.


# Filtro quer dizer que pode ou não incluir um determinado
# elemento dado na minha lista, e que pode combinar as duas
# coisas se quiser.
