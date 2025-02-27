# from aula111_A157_package.modulo import *
from sys import path

from aula111_A157_package.modulo import soma_do_modulo
# from aula111_A157_package import soma_do_modulo, fala_oi
import aula111_A157_package
import aula111_A157_package.modulo

print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula111_A157_package.modulo.soma_do_modulo(1, 2))
print(soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)

# from aula111_A157_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# fala_oi()

# import aula111_A157_package


# print(aula111_A157_package.soma_do_modulo(2, 3))

print(soma_do_modulo(2, 3))
# fala_oi()
