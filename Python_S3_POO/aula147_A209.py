# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2025    # atributo de classe
    # Atributos como este estão fora dos métodos

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#   O método é decorado com @classmethod que permite
#   que seja informmada a classe sem informar o 'self'.
#   Permite que o método se torne um método de classe
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
#   Factories method que cria um novo objeto
#   com alguma coisa arbitrária.
#   Não tem acesso a instância, pois a classe
#   está sendo diretamente chamada.

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()
