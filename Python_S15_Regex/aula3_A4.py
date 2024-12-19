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
João trouxe       flores para sua amada namorada em 10 de Janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão
de queijo.
Não canso de ouvir a Maria:
"Joooooooãoooooo, o café tá prontinho aqui. Veeemm veeem vem"!
Jã
'''

# print(re.findall(r'jo+ão+', texto, flags=re.I))
# O quantificado está aplicado a tudo o que está a sua esquerda
# print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.I))
# O quantificador + é para o item que existe apenas uma vez.
# print(re.sub(r'jo*ão*', 'Felipe', texto, flags=re.I))
# O quantificador * é para itens que aparecem infinitas vezes.
# print(re.sub(r'jo?ão*', 'Felipe', texto, flags=re.I))
# O quantificador ? é para indicar que o item pode ou não existir.
# print(re.sub(r'jo{1,n}ão{1,n}', 'Felipe', texto, flags=re.I))
# O quantificador {1,n} pode informar a quantidade de vezes que o item aparece.
print(re.findall(r'j[a-zA-Z]ão+', texto, flags=re.I))
print(re.findall(r'j[o]ão+', texto, flags=re.I))
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

texto2 = 'João ama ser amado'
print(re.findall(r'ama', texto2, flags=re.I))
print(re.findall(r'ama[do]*', texto2, flags=re.I))
print(re.findall(r'ama[od]{1,2}', texto2, flags=re.I))
print(re.findall(r'ama[do]{2}', texto2, flags=re.I))
