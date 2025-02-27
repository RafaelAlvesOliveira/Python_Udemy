import sys

# Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)   # .__iter__()  # tem __iter__ e __next__

# generator = [ n for n in range(10)]
lista = [n for n in range(10000)]
generator = (n for n in range(10000))  # generator expression

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

# for n in generator:
#     print(n)

# Generator é uma função que sabem pausar em
# determinada ocasião.

# Iterator é uma classe que tem o método iter e
# o método next, e o iterator trabalha com um
# iterável. Todo generator é um iterator,
# mas o iterator não é um generator.
