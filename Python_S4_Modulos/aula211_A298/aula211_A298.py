# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
# import json
# import os
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula211_A29.txt'

# Essa é uma alternativa ao pathlib, usando o módulo os

# caminho = os.path.join(
#     'c:', 'Users', 'Rafael Alves', 'Documents', 'Rafael', 'VSCode',
#     'PYTHON', 'Python_S4_Modulos', 'aula211_A298', 'aula211_A298.txt')

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2025, 5, 23)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    # telefone='+55 (11) 7890-5432'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))

# texto = '''
# Prezado(a) $nome,

# Informamos que sua mensalidade será cobrada no valor de ${valor} no
# dia $data. Caso deseje cancelar o serviço, entre em contato com a
# $empresa pelo telefone $telefone.

# Atenciosamente,

# ${empresa},
# Abraços
# '''


class MyTemplate(string.Template):
    delimiter = '%'

# Ao usar o delimitado é necessário que todos os locais em que esteja o "$"
# deve ser substituído por "%".


try:
    with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
        template = MyTemplate(texto)
        # template = string.Template(texto)
        try:
            print(template.substitute(dados))
        except KeyError as e:
            print(f"Erro: Variável faltando no dicionário 'dados': {e}")
        # print(template.safe_substitute(dados))
except FileNotFoundError:
    print(f'ERRO: Arquivo não encontrado em {CAMINHO_ARQUIVO.absolute()}')
    print('Certifique-se que:')
    print('1. O arquivo existe no local indicado')
    print(
        '2. O nome do arquivo está correto (incluindo maiúsculas/minúsculas)'
    )
    exit(1)
    # O número "0" indica sucesso, qualquer número diferente indica que o
    # programa foi encerrado com erro.
