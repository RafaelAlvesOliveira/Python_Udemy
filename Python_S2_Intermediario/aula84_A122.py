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

import copy
# Se quiser ou for necessário fazer uma cópia é necessário
# importar esse método do python, para que seja possível
# fazer uma cópia profunda. Esse método tem dois tipos de
# funções para copiar, 'shallow copy' que é para a cópia rasa e
# 'deep copy' que é cópia profunda.

# Shallow copy

d1 = {
    'c1': 1,
    'c2': 2,
    'li': [0, 1, 2],
}

d2 = d1

# Quando se usa o sinal de atribuição com valores mutáveis
# em listas e dicionários, ele não faz a cópia, ele simplesmente
# indica que 'd2' aponta para o mesmo dicionário de 'd1'.

# d2 = d1.copy()

# Fazer uma cópia rasa, quer dizer que será feita uma cópia de tudo
# o que for imutável. Mas se houver qualquer valor mutável não será
# feita a cópia, o python fará com que os dois dicionários apontem
# para a mesma lista na memória. Por isso o nome 'shallow copy'
# (cópia rasa), pois os subníveis não são acessados.

d2 = copy.deepcopy(d1)

# Ao utilizar o comando 'deepcopy' não ocorre mais o problema de alterar
# uma lista e afetar a outra, pois o comando consegue acessar todos
# os subníveis, ou seja, tudo que é mutável.

d2['c1'] = 1000
d2['li'][1] = 999999

print(d1)
print(d2)

# Ao alterar 'd2', 'd1' também é afetado.

# pessoa = {
#     'nome': 'Rafael',
#     'sobrenome':'Alves',
#     'idade': 100,
# }
