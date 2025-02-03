# Ordem dos decoradores

def parametros_decoradores(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametros_decoradores(nome='5')
@parametros_decoradores(nome='4')
@parametros_decoradores(nome='3')
@parametros_decoradores(nome='2')
@parametros_decoradores(nome='1')
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
