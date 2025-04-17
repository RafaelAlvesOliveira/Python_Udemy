# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


class Caneta:
    def __init__(self, cor):
        # public protected public
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
        # return 'Qualquer coisa'

    @property
    def cor_tampa(self):
        return 123456

# Usar @property ajuda a evitar a quebra de código
# pois é possível proteger um atributo dentro da classe.
# Pode ser utilizado no lugar do getter, pois faz o método
# ou função se comportar como um atributo.

##############################


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)


###################################

# class Caneta:
#     def __init__(self, cor):
#         # public protected public
#         self.cor = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor

##############################

# caneta = Caneta('Azul')
# print(caneta.get_cor)
# print(caneta.get_cor)
# print(caneta.get_cor)
# print(caneta.get_cor)
# print(caneta.get_cor)
# print(caneta.get_cor)
