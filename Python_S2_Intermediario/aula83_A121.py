# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Alves',
    'idade': 100,
}

# print(pessoa['idade'])

# Se forem criadas chaves com o mesmo valor, o python
# irá atualizar os valores e usar o último.


# len

# print(len(pessoa))
# print(pessoa.__len__())

# keys

# for chave in pessoa.keys():
#     print(chave)

# print(tuple(pessoa.keys()))
# print(list(pessoa.keys()))


# dict_keys, dict_values e dict_items, podem ser convertidos
# em tuplas, em listas, etc.

# values

# for valor in pessoa.values():
#     print(valor)

# print(list(pessoa.values()))

# items

# print(list(pessoa.items()))

# for chave, valor in pessoa.items():
#     print(chave, valor)

# setdefault - adiciona valor se a chave não existe

pessoa.setdefault('idade', None)
print(pessoa['idade'])
