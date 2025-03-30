# Criando Exceptions em Python Orientado a Objetos
 # Para criar uma Exception em Python, você só
 # precisa herdar de alguma exceção da linguagem.
 # A recomendação da doc é herdar de Exception.
 # https://docs.python.org/3/library/exceptions.html
 # Criando exceções (comum colocar Error ao final)
 # Levantando (raise) / Lançando (throw) exceções
 # Relançando exceções
 # Adicionando notas em exceções (3.11.0)
class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('você errou isso')
    # exception_ = MeuError('A mensagem do meu erro')
    raise exception_
    # raise MeuError('A mensagem do meu erro')

try:
    # 1/0
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    # exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error

# O "error" armazena as informações do erro em Args.

# Agora é possível criar notas para as exceções, afim de
# comunicar informações importantes para outros desenvolvedores
# ou para mim mesmo.
