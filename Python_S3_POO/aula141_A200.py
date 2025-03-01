# Métodos em instâncias de classes Python
# Hard Coded - É algo que foi escrito diretamente no código
# Classe - Molde (sem dados)
# Instância da classe (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

# Classe é um molde que gera novos objetos
# Instância e objeto se refere a mesma coisa
# Método é uma função dentro da classe
# Self é o mesmo que o objeto fora da classe, pois se refere
# a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
# Carro.acelerar(fusca)

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
# Carro.acelerar(celta)
