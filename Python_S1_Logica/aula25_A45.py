"""
Formatação básica de strings
s - strings
d - int
f - float
<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a __repr__ __str__
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
# Preenche com 10 caracteres (espaços) antes da variável
print(f'{variavel: <10}.')
# Preenche com 10 caracteres (espaços) depois da variável
print(f'{variavel: ^10}.')
# print(f'{variavel:$^10}.')
# print(f'{variavel:0^10}.')
# print(f'{1000.4873648123746:,.1f}')

print(f'{variavel!r}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{1000.4873648123746:0=+10,.1f}')
# Uma casa decimal após a vírgula
print(f'{1000.4873648123746:0>10,.1f}')
print(f'{-1000.4873648123746:+,.1f}')
# É possível colocar o sinal de positivo ou negativo
print(f'{1000.4873648123746:+,.1f}')
print(f'{1000.4873648123746:.1f}')
