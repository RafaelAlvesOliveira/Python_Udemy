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

# with open(caminho_arquivo, 'w') as arquivo:
#     print('Olá mundo')
#     print('Arquivo vai ser fechado.')

# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('Linha 1\r\n')
#     arquivo.write('Linha 1\r\n')

# print('#' * 20)

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
# Pode ser incluído o caractere \r\n para quebra de linha duas
# duas vezes consecutivas, pois ambos tem a mesma função.
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
# É utilizada para mover o cursor dentro do arquivo
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline())
# Comando utilizado para se ler apenas uma linha
    print(arquivo.readline(), end='')
# Pode ser utilizado o end para corrigir a quebra de linha
    print(arquivo.readline().strip())
# O comando strip pode ser utilizado para remover espaços
# do início e do fim.
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('#' * 20)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
