# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

import re

# findall => busca todas as ocorrências da expressão que precisa ser
# verificada dentro do texto
# search => vai retrnar a primeira ocorrência
# sub => serve para substituir alguma coisa dentro do texto
# compile => compilar expressões regulares, é útil para reutilizar as mesmas

# Teste e teste são duas palavras diferentes

string = 'Este é um teste de expressões regulares, teste.'
print(re.search(r'teste', string))
print(re.search(r'teste2', string))
# Caso não encontre a expressão solicitada retorna none.

print(re.findall(r'teste', string))
print(re.findall(r'teste2', string))
# Caso não encontre a expressão retorna []

print(re.sub(r'teste', 'ABCD', string))
# Substitui a palavra 'teste' por ABCD
print(re.sub(r'teste', 'ABCD', string, count=0))
# O padrão é "0" é utilizado para substituir todas.
print(re.sub(r'teste', 'ABCD', string, count=1))
# Substitui apenas a primeira palavra, as demais não

regexp = re.compile(r'teste')
# Compila a expressão regular, e depois reutiliza a mesma.
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))
