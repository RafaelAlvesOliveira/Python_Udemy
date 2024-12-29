"""
Higher Order Function
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)


# v = executa(saudacao, 'Bom dia', 'Rafael')


print(
    executa(saudacao, 'Bom dia', 'Rafael')
)

print(
    executa(saudacao, 'Bom dia', 'Maria')
)


# print(v)

# v = saudacao('Bom dia')
# print(v)
