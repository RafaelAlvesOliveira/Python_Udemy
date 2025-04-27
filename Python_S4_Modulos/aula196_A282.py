# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

# Une as strings para formar o caminho relativo para o arquivo.
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
# caminho = os.path.join('Documents', 'Desktop', 'curso', 'arquivo.txt')
# print(caminho)

# Divide o diretorio e a extensão do arquivo em duas tuplas
diretorio, arquivo = os.path.split(caminho)
# print(arquivo)
# print(diretorio)

# Separa o caminho do arquivo da sua extensão.
caminho_arquivo, extensao_arquivo = os.path.splitext(caminho)
# print(caminho_arquivo, extensao_arquivo)

# Realiza a separação entre o nome do arquivo e a extensão
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
# print(nome_arquivo, extensao_arquivo)

# Verifica se o caminho informado realmente existe.
# print(os.path.exists('C:\\Users\\Rafael Alves\\Documents\\Rafael\\VSCode'))

# Retorna o caminho absoluto desta pasta
# print(os.path.abspath('.'))

# Mostra apenas a parte final do caminho
# print(os.path.basename(caminho))
# print(os.path.basename(diretorio))

# Retorna o diretorio do arquivo de acordo com o que foi
# informado na variável caminho
print(os.path.dirname(caminho))
