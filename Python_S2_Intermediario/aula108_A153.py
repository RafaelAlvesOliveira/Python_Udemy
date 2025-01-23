# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# import sys

# platform = 'a minha'
# print(sys.platform)
# print(platform)

# para utilizar o módulo sys é necessário utilizar
# o 'name space' do módulo.

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# from sys import exit, platform

# print('bla')
# exit()

# Se atentar para não colocar o mesmo de módulos
# em variáveis, pois isso vai sobrescrever o módulo

# alias 1 - import nome_modulo as apelido
# import sys as s
# sys = 'alguma coisa'
# print(s.platform)
# print(sys)

# se não for possível mudar o nome da variável, existe
# a possibilidade de colocar um alias (as) ou apelido
# na variável

# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

# from sys import *

# print(platform)
# exit()

# É uma má prática importar todas as funções do
# módulo sys
