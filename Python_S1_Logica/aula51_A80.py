"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

# ........01234
# ........54321
string = 'ABCDE'   # 5 caracteres
# lista = list()
# lista = []
# print(bool([]))   # false
# print(lista, type(lista))

#  .......0....1.....2........3....4
#  ......-5...-4....-3.......-2...-1
lista = [123, True, 'Rafael', 1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2].upper(), type(lista[2]))
