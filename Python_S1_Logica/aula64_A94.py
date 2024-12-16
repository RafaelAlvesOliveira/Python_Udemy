"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena',],  # 0
    # 0
    ['Elaine',],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda'],    # 2
    # ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], # 2
]

# print(salas[1])
# O valor mostra a lista [1]
# print(salas[1][0])
# Será apresentada a lista [1] e o valor [0] que
# corresponde a Elaine
# print(salas[0][1])
# Será apresentada a lista [0] e o valor [1] que
# corresponde a Helena
# print(salas[2][2])
# Será apresentada a lista [2] e o valor [2] que
# corresponde a Eduarda
# print(salas[2][3][2])
# Será apresentada a lista [2] e o valor [3] e
# dentro da tupla acessar o valor 20 que
# corresponde ao índice [2]

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

# O primeiro for é para a primeira lista, e o
# # segundo for é para os alunos dentro das listas
# internas.
