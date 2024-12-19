# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] Conjunto de caracteres
import re

texto = '''
João trouxe       flores para sua amada namorada em 10 de Janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão
de queijo.
Não canso de ouvir a Maria:
"Joooooooãoooooo, o café tá prontinho aqui. Veeeemm"!
'''

print(re.findall(r'João|Maria|adultos', texto))
print(re.findall(r'João|Maria|ad....s', texto))
# o . (ponto) significa qualquer caractere.
print(re.findall(r'João|joão|Maria', texto))
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
# É utilizado o conjunto com as letras minúsculas e maiúsculas
print(re.findall(r'[a-z]aria', texto))
print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão', texto))
# Podem ser utilizados ranges para buscar tanto números como letras
print(re.findall(r'jOãO|mAriA', texto, flags=re.I))
# É possível usar as 'flags' como I oui IgnoreCase para procurar a informação
# independente de como ela apareça.
