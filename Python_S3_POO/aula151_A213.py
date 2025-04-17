# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        # print('PROPERTY')
        print('Estou no Getter')
        return self._cor

    @cor.setter
    def cor(self, valor):
        # if valor == 'Rosa':
        #     raise ValueError('Não aceito essa cor')
        # print('Estou no Setter', valor)
        print('Estou no Setter')
        self._cor = valor

# Para ter um setter é necessário ter uma @property.
# Tem que ter o .self

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


# def mostrar(caneta):
#     return caneta.cor

# Setter é usado para configurar valores diferentes
# para um determinado atributo.

caneta = Caneta('Azul')
caneta.cor = 'Rosa'
# caneta.cor = 'Pink'
# caneta.cor_tampa = 'Azul'
print(caneta.cor)
# print(caneta.cor_tampa)

# getter -> obter valor
# print(caneta.cor)
