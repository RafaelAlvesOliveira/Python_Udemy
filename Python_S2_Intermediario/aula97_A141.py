# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

# print(produto.items())

# dc = {
#     chave: valor
#     if isinstance(valor, (int, float)) else valor.upper()
#     for chave, valor
#     in produto.items()
# }

# dc = {
#     chave: valor.upper()
#     if isinstance(valor, str) else valor
#     for chave, valor
#     in produto.items()
#     if chave != 'categoria'
#     # if chave == 'categoria'
# }

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

# print(dict(lista))
# print(dc)

s1 = {2 ** i for i in range(10)}
print(s1)


# s1 = {i for i in range(10)}
# print(set(range(10)))
