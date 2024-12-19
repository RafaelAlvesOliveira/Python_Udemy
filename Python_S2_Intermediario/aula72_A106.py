'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''


def soma(x, y, z):
    # Definição
    print(f'{x=} e y={y} z ={z}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
# Estão sendo passados argumentos posicionais
# para x e y.

soma(1, y=2, z=5)

print(1, 2, 3, sep='-')
# soma(y=2, z=3, x=1)
