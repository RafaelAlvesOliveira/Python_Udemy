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

caminho_arquivo = 'aula130_A186.txt'

# Se for utilizado o comando acima será criado
# um arquivo dentro da pasta, que o arquivo com
# script está sendo executado. Se não for especificado
# onde o arquivo deve ser aberto, será aberto na mesma
# pasta.

caminho_arquivo = 'C:\\Users\\Rafael Alves\\Documents\\Rafael'
caminho_arquivo += '\\VSCode\\PYTHON_UDEMY\\aula186.txt'
# Se for passar um caminho completo, é necessário colocar
# duas barras.

# arquivo = open(caminho_arquivo, 'r') # r significa read (leitura)
# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()
