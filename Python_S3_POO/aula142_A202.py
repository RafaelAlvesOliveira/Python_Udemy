# Escopo da classe e de métodos da classe

class Animal:
    # nome = 'Leão'

    # Todas as variáveis que estão dentro do __init__, não podem
    # ser acessados de fora desse método.
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
        # print(f'{self.nome} está executando uma ação')

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
# print(leao.comendo('maçã'))
print(leao.executar('maçã'))
