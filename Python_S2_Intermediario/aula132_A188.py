# Leia também:
# https://www.otaviomiranda.com.br/2020/
# normalizacao-unicode-em-python/
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# A diferença entre 'w' e 'a', é que o w apaga tudo
# o que estiver no arquivo e escreve o que for enviado.

caminho_arquivo = 'aula130_A186.txt'

# É necessário usar encoding = 'utf-8' para alterar
# a codificação do sistema.

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# O 'a' não apaga nada do arquivo e começa a escrever
# a partir da última linha do arquivo.

# with open(caminho_arquivo, 'a') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )

# O 'b' seria para abrir o arquivo em modo binário.

# with open(caminho_arquivo, 'b') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
