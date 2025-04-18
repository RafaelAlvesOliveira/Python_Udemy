# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass

# Caso não queira usar o order, posso criar a minha própria ordenação
# utilizando lambda


@dataclass(repr=True)
# @dataclass(repr=True, order=True)
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    # ordenadas = sorted(lista, reverse=True)
    ordenadas_nome = sorted(lista, reverse=False, key=lambda p: p.nome)
    ordenadas_sobrenome = sorted(
        lista, reverse=False, key=lambda p: p.sobrenome)
    print(ordenadas_nome)
    print(ordenadas_sobrenome)


# Frozen serve para congelar a classe, ou seja, não é possivel setar nada.

# @dataclass(frozen=True)
# class Pessoa:
#     nome: str
#     sobrenome: str

# É uma boa prática sempre criar uma nova variável, método ou função a ter que
# alterar uma existente.


# if __name__ == '__main__':
#     p1 = Pessoa('Rafael', 'Alves')
#     p1.nome = 'Maria'
#     print(p1)
