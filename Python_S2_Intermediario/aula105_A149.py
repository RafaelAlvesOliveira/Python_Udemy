# Try, except, else e finally

# a = 18
# b = 0
# c = a / b

string = 'Rafael'   # str
print(isinstance(string, str))

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    # print('Dividiu por zero')
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('Msg: ', error)
    # Mensagem para saber o tipo de erro
    print('Name: ', error.__class__.__name__)
    # Mostra o nome do tipo de erro de acordo com
    # a classe do mesmo.
except Exception:
    print('Erro desconhecido')

print('Continuar')
