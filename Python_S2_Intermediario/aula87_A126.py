# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Rafael')
# s1 = {'Rafael'}

# s1 = set() # vazio
# s1 = {'rafael', 1, 2, 3} # com dados

# print(s1)
# print(s1, type(s1))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# s1 = {1, 2, 3, 3, 3, 3, 3, 1}
# print(s1)

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

# s1 = {1, 2, 3, (123,)}
# print(s1)

# s1 = {1, 2, 3}
# print(3 in s1)
# print(3 not in s1)
# print(4 in s1)
# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Rafael')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Rafael')
print(s1)
# Update pode ser utilizado para enviar vários valores
# de uma única vez, o comando add só peermite enviar um
# por vez.

# Operadores úteis:

s1 = {1, 2, 3}
s2 = {2, 3, 4}

# união | união (union) - Une

s3 = s1 | s2
print(s3)

# intersecção & (intersection) - Itens presentes em ambos

s3 = s1 & s2
print(s3)

# diferença - Itens presentes apenas no set da esquerda

s3 = s1 - s2
print(s3)

s3 = s2 - s1
print(s3)

# diferença simétrica ^ - Itens que não estão em ambos

s3 = s2 ^ s1
print(s3)
