# Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
# .__iter__()  # tem __iter__ e __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Iteravel tem a responsabilidade de armazenar os valores
# O Iterator é responsável por entregar um valor por vez.
