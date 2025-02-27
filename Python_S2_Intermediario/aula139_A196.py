# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# def soma(*args):
#     print(sum(args))

# Por usar a barra no final das declarações da função é possível
# impedir que o usuário envie argumentos nomeados.
# def soma(a, b, /, x, y):
#     print(a + b + x, y)

# def soma(a, b, *, c):
#     print(a + b + c)
# Se for usado args como mostrado no exemplo a função não irá
# funcionar, pois seria necessário enviar um argumento nomeado.
# Caso não seja enviado o script não funciona.


# soma(1)
# soma(1, 2, 3)
# soma(1, 2, c=3)


def soma(a, b, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


soma(1, 2, c=3, nome='teste')

# soma(1, 2)
# soma(x=1, y=2)

# soma(1, 2, 3, y=3)
