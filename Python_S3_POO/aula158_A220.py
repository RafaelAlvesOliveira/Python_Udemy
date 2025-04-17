# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# Built-in são métodos que já vem com o pacote da
# linguagem em python. E já faz automaticamente a herança da
# classe que eu estou criando do built-in object. O object
# cria um objeto vazio.

# Tem uma função no Python help() e dá informações detalhadas
# sobre a classe, e que a mesma herda da super classe object do python.
# help(Pessoa)

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Eita, nem saí da classe Cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'cpf aluno'
    ...


c1 = Cliente('Rafael', 'Alves')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()
print(a1.cpf)
# help(Cliente)
