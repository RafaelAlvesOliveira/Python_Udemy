# Exemplo de uso dos sets

# O objetivo é armazenar palavras ou números
# dentro do conjunto

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Parabéns!')
        break

    print(letras)
