"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Rafael'
preco = 1000.98897643
variavel = '%s, o preço total é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (15, 15))
