# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# http://brasilescola.uol.com.br/matematica/fatorial.htm

# Não executar pois irá quebrar a função devido ao limite
# que a call stack suporta.

# import sys
# sys.setrecursionlimit(1004)

# def recursiva(inicio=0, fim=10):
#     print(inicio, fim)
#     # Caso base
#     if inicio >= fim:
#         return fim

#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva())


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
print(factorial(100))
