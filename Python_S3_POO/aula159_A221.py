# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('Chamou Upper')
#         retorno = super(MinhaString, self).upper()
#         print('Depois do Upper')
#         return retorno
# Sobreposição de métodos com o super()
# O médoto super() recebe a classe e o primeiro argumento


# string = MinhaString('Rafael')
# print(string.upper())

class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print('Ei, burlei o sistema.')

    def metodo(self):
        # super().metodo()  # B
        # super(B, self).metodo()  # A
        # super(A, self).metodo()  # object
        A.metodo(self)
        B.metodo(self)
        print('C')
# o método super(C, self) ou super() recebe a classe e o argumento,
# e nesse caso sempre que a classe B é chamada
# é acionado o método anterior que nesse caso
# seria a classe A.


# print(C.mro())
# print(B.mro())
# print(A.mro())
# mro() significa Method Resolution Order que é
# uma lista com a ordem de execução dos métodos.

c = C('Atributo', 'Qualquer')
# print(c.atributo)
# print(c.outra_coisa)
c.metodo()
# print(c.atributo)
# c = C('Atributo')
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()
