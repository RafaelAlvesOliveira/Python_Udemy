# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# R a f a e l
# 6 5 4 3 2 1

nome = 'Rafael'
# print(nome[2])
# print(nome[-4])
# print('afa' in nome)
# print('z' in nome)
# print(10 * '-')
# print('afa' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} não está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
