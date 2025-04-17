# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass

# Frozen é usado para congelar a classe
# Uma coisa congelada é sempre uma boa prática de programação
# É melhor criar um método ou classe nova, do que ter que alterar
# uma variável existente.


@dataclass(repr=True)
# @dataclass(repr=True, order=True)
# @dataclass(frozen=True)
# @dataclass(init=False, frozen=True)
class Pessoa:
    nome: str
    sobrenome: str
    # idade: int

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self):
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'
    # print('Pós init')

    # Post init é executado após o __init__. Quando o __init__ é False, o Post
    # init não é executado, e nessa condição é necessário definir o init.

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'
    #     # return f'{self.nome} {self.sobrenome} {self.idade}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    # ordenadas = sorted(lista, reverse=True, key=lambda p: p.nome)
    print(lista)
    # p1 = Pessoa('Rafael', 'Alves')
    # p1.nome = 'Maria'
    # p1 = Pessoa('Rafael', 'Alves', 34)
    # p1.nome_completo = 'Maria Helena Figueiredo'
    # p2 = Pessoa('Rafael', 34)
    # print(p1)
    # print(p1.nome_completo)
    # print(p1 == p2)
