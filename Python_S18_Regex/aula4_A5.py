# Meta caracteres: . ^ $  ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+
import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>
'''


# print(re.findall(r'<[pdiv]{1,3}>.+<\/[pdiv]{1,3}>', texto))
# Esse seria o método Non-greedy, pois retornaria uma valor por vez.
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))
# Esse seria o método Greedy, pois retornaria todos os valores de uma vez.
# print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto))
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))
