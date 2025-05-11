# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

print(qtd_argumentos)
# print(sys.argv)

if qtd_argumentos <= 1:
    print('Você não passou argumentos.')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça alguma coisa com {argumentos[2]}')
        print(f'Faça alguma coisa com {argumentos[3]}')
    except IndexError:
        print('Faltam argumentos.')
