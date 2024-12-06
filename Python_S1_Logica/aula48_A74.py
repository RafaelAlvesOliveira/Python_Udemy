"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('rafael')            # .__iter__()

# print(next(texto))                # print(texto.__next__())
# print(next(texto))                # print(texto.__next__())
# print(next(texto))                # print(texto.__next__())
# print(next(texto))                # print(texto.__next__())
# print(next(texto))                # print(texto.__next__())
# print(next(texto))                # print(texto.__next__())

# for letra in texto
texto = 'Rafael Alves'  # iterável
# iterador = iter(texto)  #iterator

# while True:
#     try:
#         letra = (next(iterador))
#         print(letra)
#     except StopIteration:
#         break

# Isso é o que o "for" faz por debaixo dos panos.

for letra in texto:
    print(letra)
