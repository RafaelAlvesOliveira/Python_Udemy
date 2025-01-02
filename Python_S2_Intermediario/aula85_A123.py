# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# get

p1 = {
    'nome': 'Rafael',
    'sobrenome': 'Alves'
}

p2 = {
    'nome': 'Amélia',
    'sobrenome': 'Santos'
}

# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# O comando get obtém a chave do dicionário e retorna
# o nome ou valor da chave.

# pop

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# O método pop elimina a chave do dicionário, mas a mesma
# pode ser atribuída a uma variável.

# popitem

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# popitem remove a última chave do dicionário.

# update

# p1.update({
#     'nome':'novo nome',
#     'sobrenome': 'novo sobrenome',
#     'idade' : '30'
# })

# p1.update(nome='novo valor', idade='30')

# O método update atualiza as informações dentro do dicionário,
# e também através dele é possível acrescentar novas informações
# ao dicionário.

tupla = (('nome', 'novo valor'), ('idade', '30'))
p1.update(tupla)
print(p1)

lista = [['nome', 'Joaquim'], ['idade', '35']]
# p2.update(lista)
p2.update(dict(lista))
print(p2)

# Para evitar o aviso do pylance "Nenhuma sobrecarga para "update"
# corresponde aos # argumentos fornecidosPylancereportCallIssue
# # typing.pyi(752, 9): Sobrecarga 2 é a correspondência
# mais próxima. Devido a isso converti a lista em dicionário.
