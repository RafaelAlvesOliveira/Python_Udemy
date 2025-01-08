# Empacotamento e desempacotamento de dicionários

# a, b = 1, 2
# a, b = b, a
# print(a,b)

# pessoa = {
#     'nome': 'Aline',
#     'sobrenome' : 'Souza',
# }

# a, b = pessoa
# a, b = pessoa.items()
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoas = {
    'idade': 16,
    'altura': 1.6,
}

# pessoas_completa = {**pessoa, 'chave':1}
pessoas_completa = {**pessoa, **dados_pessoas}

# print(pessoa, dados_pessoas)
# print(pessoas_completa)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)
        # print(kwargs)

# mostro_argumentos_nomeados(**pessoas_completa)
# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
