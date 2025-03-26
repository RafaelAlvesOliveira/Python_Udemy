# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name
    
# Essa property pertence a essa classe, sendo assim
# a mesma será passada para a classe debaixo como
# atributo. O problema é que não é possível definir
# um setter.
    
    @name.setter
    @abstractmethod
    def name(self, name): ...

    # @property
    # @abstractmethod
    # def name(self): ...
        # return self._name

    # @name.setter
    # def name(self, name): ...
        # self._name = name


class Foo(AbstractFoo):
    # name = ''

# Criar um atributo de classe name, funciona da mesma
# forma que a @property. Pois a @property é um método
# que se comporta como atributo.
# Nota: Isso não funciona para atributos de instância 

    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name

# Isso é uma forma de forçar o programador a criar
# uma property quando ela instanciar a classe AbstractFoo

foo = Foo('Bar')
print(foo.name)
