# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

# caminho do arquivo CSV
CAMINHO_CSV = Path(__file__).parent / 'aula208_A294.csv'

lista_clientes = [
    {'Nome': 'Rafael Alves', 'Endereço': 'Av. 1, 23'},
    {'Nome': 'João Silva', 'Endereço': 'R. 3, "4"'},
    {'Nome': 'Maria Rosa', 'Endereço': 'Av. A, 5A'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)

# Lista com nomes de clientes fictícios
# lista_clientes = [
#     ['Rafael Alves', 'Av. 1, 23'],
#     ['João Silva', 'R. 3, "4"'],
#     ['Maria Rosa', 'Av. A, 5A'],
# ]

# Abrir e escrever informações dentro do arquivo.
# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo,)

#     escritor.writerow(nome_colunas)

#    for cliente in lista_clientes:
#        print(cliente.values())
#        escritor.writerow(cliente.values())

#    for cliente in lista_clientes:
#        escritor.writerow(cliente)
