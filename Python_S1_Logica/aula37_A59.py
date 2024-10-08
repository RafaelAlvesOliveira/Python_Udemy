"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

condicao = True

while condicao:
    nome = input('Qual é o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')
# print(123) # Trecho de código que não pode ser executado se o loop "for"
# infinito.
