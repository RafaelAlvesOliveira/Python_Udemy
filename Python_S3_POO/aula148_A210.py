# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classe:
    @staticmethod
    # Método estático é uma função dentro da classe
    # Ele não tem acesso a nada.
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)


def funcao(*args, **kwargs):
    print('Oi', args, kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
funcao(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado=1)
funcao(nomeado=1)
# O static method faz mesma coisa que a função,
# a única diferença é que a função fica protegida
# pela classe.
