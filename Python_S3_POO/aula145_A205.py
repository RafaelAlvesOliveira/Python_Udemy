# __dict__ e vars para atributos de instância:

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)
# p1 = Pessoa('João', 35)
# p1.nome = 'Eita'
# print(p1.nome)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# Os valores que são utilizados para criar um novo objeto
# estão salvos dentro do dicionário __dict__. O método "vars"
# mostra os valores que estão salvos no dicionário.
# print(p1.outra)
# print(p1.nome)
print(vars(p1))
print(p1.nome)
