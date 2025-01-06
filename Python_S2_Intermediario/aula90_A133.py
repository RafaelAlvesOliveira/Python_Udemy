# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista.sort(reverse=True)
# sorted(lista)
# Faz a mesma coisa, a diferença é que é feita
# uma cópia rasa (shallow copy)

lista = [
    {'nome': 'Rafael', 'sobrenome': 'Alves'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'}
]


# def ordena(item):
#    print(item)
#    return item['nome']
#    return item['sobrenome']

# lista.sort(key=ordena)
# print(lista)

# lista.sort(key=lambda item: item['nome'])

# for item in lista:
#     print(item)

def exibir(lista):
    for item in lista:
        print(item)


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
