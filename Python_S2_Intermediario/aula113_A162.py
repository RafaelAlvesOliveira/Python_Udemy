# Exercício - Adiando execução de funções

def soma(x, y):
    return x + y


def multiiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiiplica, 10)
print(soma_com_cinco(10))
print(multiplica_por_dez(10))
