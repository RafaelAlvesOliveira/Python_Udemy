"""
Retorno de valores das funções (return)
"""

# Só funções e métodos tem a palavra 'return'.
# Não é possível executar nada após o 'return'.
# O return só pode retornar um valor por função.


def soma(x, y):
    if x > 10:
        return 10, 20
    return x + y
    # print(x + y)

# variavel = soma(1, 2)
# variavel = int('1')


soma1 = soma(2, 2)
soma2 = soma(3, 3)

# Esse print só funciona se houver o parâmetro
# return na função, caso contrário não funciona

# print(soma1 + soma2)
print(soma1)
print(soma2)
print(soma(11, 55))

# Esse print não funciona, pois não pode retornar a
# soma de dois valores 'NoneType', pois é necessário
# fazer um return dos valores de 'soma' para cada uma
# das variáveis

# variavel = print('Rafael')
# print(variavel)

# None significa não valor

# variavel = None
# print(variavel is None)
