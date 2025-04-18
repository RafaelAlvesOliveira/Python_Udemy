# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    # Object é a úlitma classe por assim dizer, sendo assim
    # a classe herda de Object. Não é necessário escrever Object
    # na classe.
    def __new__(cls, *args, **kwargs):
        # print('Antes de criar a instância')
        instancia = super().__new__(cls)
        # print('Depois')
        # instancia.x = 213
        return instancia
        # return object.__new__(A)
        # Em vez de usar o object nos metodos da classe, podemos
        # usar o super.

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'
    

a = A(123)
print(a)
print(a.x)
# a = object.__new__(A)
# a.__init__()
# print(a)
# Ao iniciar um objeto o primeiro método chamado é o __new__
