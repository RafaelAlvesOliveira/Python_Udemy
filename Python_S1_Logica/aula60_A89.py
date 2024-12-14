"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joaquim')

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

# for item in lista_enumerada:
#     print(item)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)
#     print(item)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# Faz a mesma coisa que o exemplo anterior, mas a 
# diferença é que faz o desempacotamento junto com
# o "for", ou seja, é como se tivesse um "for" dentro
# do outro.

# for item in enumerate(lista):
#     for valor in item:
#         print(valor)

# for tupla_enumerada in enumerate(lista):
#     print('For da tupla: ')
#     for valor in tupla_enumerada:
#         print(f'\t{valor} ')

# Esse exemplo faz a mesma coisa uqe o exemplo acima, a
# diferença é que no outro exemplo está simplificado.

# o barra "\t" é o equivalente ao "tab"
