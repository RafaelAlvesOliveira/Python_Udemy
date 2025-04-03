# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...
# class MyContextManager:
class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
        # print('INIT')

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf-8')
        return self._arquivo
        # print('ENTER')
        # return 1234
    # O retorno do ENTER vai para a variável "alguma_coisa"

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)
        # raise class_exception('Minha mensagem')

        # print(class_exception)
        # print(exception_)
        # print(traceback_)

        # exception_.add_nota('Minha nota')
        return True

        # raise ConnectionError('Não deu para conectar')
        # Tratei a exceção
        # print('EXIT')


# instancia = MyContextManager('aula149.txt', 'w')

# with MyContextManager() as alguma_coisa:
# Se fosse feito dessa forma funcionaria do mesmo jeito.
# with instancia as alguma_coisa:
    # print('WITH', alguma_coisa)

with MyOpen('aula169_A240.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
