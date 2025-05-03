from pathlib import Path

caminho_projeto = Path()
# Para que o caminho completo apareça é necessário
# executar o método absolute().
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# Através do __file__ é possível encontrar o caminho
# completo até o arquivo.
print(caminho_arquivo)

# Ao usar .parent é possível ver o caminho absoluto até a pasta pai,
# caso seja utilizado consecutivamente é possível ver as pastas em
# níveis acima.
print(caminho_arquivo.parent)
# print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivo.txt')
# Todas as pastas informadas não estão sendo salvos em sistema.
