# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

# string = 'Rafael'    # str
# É uma instância de str
# print(string.upper())
# upper() é um método que altera a string que selecionei
# print(isinstance(string, str))
# isinstance checa se a string é a instância da classe str
# A classe str é responsável por saber que o dado que está
# dentro da variável 'string'


# Esse molde pode gerar novos objetos
# Os dados dentro da classe são atributos
# As ações que são executadas dentro da classe são
# funções, são chamadas de métodos.
# O primeiro parâmetro deve ser self, para referenciar a
# instância atual da classe e é usado para acessar variáveis que
# pertencem a mesma.
# Cada um dos objetos terá seu próprio self dentro da classe.
class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


# Esse objeto poderia criar uma nova instância da classe Pessoa
p1 = Pessoa('Rafael', 'Alves')
# p1.nome = 'Rafael'
# p1.sobrenome = 'Alves'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

# O print mostrar que p1 já é uma instância da classe Pessoa
print(p1)
print(p1.nome)
print(p1.sobrenome)

print(p2)
print(p2.nome)
print(p2.sobrenome)
