import os

# Leia também:
# https://www.otaviomiranda.com.br/2020/
# normalizacao-unicode-em-python/
# with open (context manager) e métodos úteis do TextIOWrapper
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

caminho_arquivo = 'aula130_A186.txt'

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.remove(caminho_arquivo)
os.unlink(caminho_arquivo)

# as funções remove e unlink são utilizados para remover um
# arquivo.

os.rename(caminho_arquivo, 'aula130_A186-2.txt')

# é utilizado para renomear o arquivo.
