# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 2134


call1 = CallMe('238458765545')
retorno = call1('Rafael')
# O método Call faz a instância (objeto da classe) ser executável.
print(retorno)
