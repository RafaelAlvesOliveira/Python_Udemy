# Introdução às Generator functions em Python
# generator = (n for n in range(100000))

# def generator(n=0):
#     yield 1  # Pausar
#     print('Continuando...')
#     yield 2  # Pausar
#     print('Mais uma vez...')
#     yield 3
#     print('Vou terminar')
#     return 'Acabou'


def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return


# O 'yield' substitui o 'return'
# Dentro da generator function o 'return
# levanta uma exceção de StopIteration

# gen = generator(n=5, maximum=8)
gen = generator(maximum=100)

for n in gen:
    print(n)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
