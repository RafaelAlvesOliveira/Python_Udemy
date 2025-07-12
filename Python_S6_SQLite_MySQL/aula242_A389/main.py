import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Cuidado: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
cursor.execute(
    f'INSERT INTO {TABLE_NAME} '
    '(id, name, weight) '
    'VALUES '
    '(NULL, "Gabriela", 4), (NULL, "Rafael", 9.9)'
)

# CUIDADO: SQL Injection
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(id, name, weight) '
#     'VALUES '
#     '(:nome, :peso)'
# )
# cursor.executemany(sql, [['Joana', 4], ['Rafael', 5]])
# cursor.executemany(
#     sql,
#     (
#         ('Joana', 4), ('Rafael', 5)
#     )
# )
# Sintax não reconhecida pelo DBeaver da versão mais recente.
# cursor.execute(sql, {'nome': 'Sem nome', 'peso': 3})
# cursor.executemany(sql, (
#     {'nome': 'Joãozinho', 'peso': 3},
#     {'nome': 'Maria', 'peso': 2},
#     {'nome': 'Helena', 'peso': 4},
#     {'nome': 'Joana', 'peso': 5},
# ))
connection.commit()
# print(sql)

cursor.close()
connection.close()
