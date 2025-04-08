# Classes decoradoras (Decorator classes)
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador
        # self.func = func

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna
        # return resultado * self._multiplicador


# Quando o decorador estiver em letra maiúscula quer
# dizer que é uma classe decoradora em vez de uma função
@Multiplicar(10)
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2,4)
print(dois_mais_quatro)

# dois_mais_dois = soma(2,2)
# print(dois_mais_dois)
