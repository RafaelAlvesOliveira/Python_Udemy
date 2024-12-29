# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'
# create => criação de chave
pessoa[chave] = 'Rafael'
pessoa['sobrenome'] = 'Alves'

print(pessoa[chave])
# edit => edição de chave
pessoa[chave] = 'Maria'

# del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa['sobrenome'])

# print(pessoa.get('sobrenome'))

# if pessoa['sobrenome']:
if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
# print('Isso não vai')

# Não é possível acessar uma chave que não existe
# no dicionário, mas é possível criar uma chave
# com o sinal de atribuição.
