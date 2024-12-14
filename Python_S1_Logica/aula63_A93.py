"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = '   Olha só que   , coisa interessante    '
lista_frases_cruas = frase.split(',')

# for i, frase in enumerate(lista_frase):
#     print(lista_frase[i].strip())

# rstrip retira o espaço da direita
# lstrip retira o espaço da esquerda

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)

# o 'join' serve para unir a(s) listas, e também pode ser
# definido um separador. É necessário criar uma string vazia
# para fazer a separação dos itens iteráveis, apenas iteráveis.
# Só pode ser usado com lista, strings e tuplas.