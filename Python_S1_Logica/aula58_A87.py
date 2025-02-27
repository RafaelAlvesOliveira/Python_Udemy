"""
Introdução ao desempacotamento + tuples (tuplas)
"""

# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2 = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Luiz']

# # Se houver menos variáveis do que a quantidade de valores
# o python irá apresentar um erro. E o contrário também, se
# houver mais variáveis do que valores será apresentado outro
# erro.

# nome1, *resto = ['Maria', 'Helena', 'Luiz']
# print(nome1, resto)

# Caso seja necessário pegar apenas o primeiro valor, pode
# ser criada uma variável de resto, para empacotar o restante
# dos valores.

# nome1, *_ = ['Maria', 'Helena', 'Luiz']
# print(nome1)

# Uma outra convenção do python é usar o _(underline) após
# o asterisco para indicar que essa variável está armazenando
# o restante dos valores.

# _, nome2, *_ = ['Maria', 'Helena', 'Luiz']
# print(nome2)

# Se for necessário pegar qualquer outro valor que não seja
# nem o primeiro nem o último, é só acrescentar o _(underline)
# como se primeiro valor.

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, resto)

# Mesmo não tendo mais valores após, a variável "resto"
# ainda assim funciona, será armazenada uma lista vazia.
