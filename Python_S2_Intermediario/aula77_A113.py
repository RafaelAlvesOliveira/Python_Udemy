# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)
print(1*2*3*4*5)


def impar_par(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} par'
    return f'{numero} é impar'


print(impar_par(2))
print(impar_par(3))
print(impar_par(15))
print(impar_par(16))


# def par_impar(numero):
#     numero = int(numero)
#     numero_digitado = numero % 2 == 0

#     if numero_digitado:
#         return f'Número é par {numero}'
#     else:
#         return f'O número é ímpar {numero}'


# numero = input('Digite o número: ')
# print(par_impar(numero))

# print(par_impar(5))
# print(par_impar(100))
