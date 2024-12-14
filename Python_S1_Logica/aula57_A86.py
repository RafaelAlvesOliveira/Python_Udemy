"""
Exercício
Exiba os índices da lista
"""

lista = ['Maria', 'Helena', 'Rafael']
lista.append('João')

indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))


i = 0
while i < len(lista):
    for nome in lista:
        print(i, nome)
        i += 1
    break
