""" while / else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

# Quando houver um break dentro do while
    # o loop será quebrado, e o else não será
    # executado.

    if letra == ' ':
        break
    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
    print('O else foi executado.')
print('Fora do while.')
