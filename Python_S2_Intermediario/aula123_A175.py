# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome': 'Rafael', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena(aluno):
    return aluno['nota']


# alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])
alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
#   print(list(grupo))


# for aluno in alunos_agrupados:
#     print(aluno)


# alunos = ['a', 'a', 'a', 'a', 'b', 'c', 'a']
# grupos = groupby(sorted(alunos))
