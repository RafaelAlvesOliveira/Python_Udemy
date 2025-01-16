# dir, hasatrr e getattr em Python

string = 'Rafael'
# metodo = 'upper'
metodo = 'lower'
# metodo = 'strip'

# print(string)

# dir mostra todos os nomes de métodos definidos dentro de string.

# getattr checa dinamicamente se o objeto tem um determinado atributo

# hasattr checa se um determinado objeto tem um determinado nome dentro dele

if hasattr(string, metodo):
    print('Existe o método', metodo)
    print(getattr(string, metodo)())
    # print(string)
else:
    print('Não existe o método ', metodo)
