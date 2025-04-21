# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# fmt = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2025-4-17 10:35:43', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%m'), data.month)
print(data.strftime('%d'), data.day)
print(data.strftime('%H'), data.hour)
print(data.strftime('%m'), data.minute)
print(data.strftime('%S'), data.second)

# O tipo de data é em string, é necessário ter cuidado visto não ser
# um número. Formato sempre se trata de string.
print(type(data.strftime('%Y')))
# print(data)
