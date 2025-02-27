# Count é um iterator sem fim

from itertools import count

c1 = count(step=8, start=8)
r1 = range(8, 100, 8)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')

for i in c1:
    if i >= 100:
        break
    print(i)

print()
print('range')

for i in r1:
    if i > 100:
        break
    print(i)

# Count é um contador infinito, pois não é informado o valor
# limite para contagem.
# Range é um contador finito, pois é informado até que valor
# deve ser feita a contagem.
