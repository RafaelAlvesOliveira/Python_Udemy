"""
Tipo Tupla - Uma lista imutável
"""

# lista
nomes = ['Maria', 'Helena', 'Luiz']

# tupla
nome = 'Maria', 'Helena', 'Luiz'
# Uma tupla não tem colchetes, é opcional colocar
# os parênteses

# nome[1] = 'outro'
# não é possível alterar valores nas tuplas
# print(nome, nome1)

# print(nome[0], nome[-1])
# print(nome)

# É possível acessar os valores dentro da tupla da
# mesma forma que é feito com listas.

nomes = tuple(nome)
print(nomes)
nomes = list(nomes)
print(nomes)

# É possível converter uma tupla em uma lista e
# vice-versa
