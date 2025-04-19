# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

data_str_data = '2025-04-14 23:37:35'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

data_str_data_br = '14/04/2025'
data_str_fmt_br = '%d/%m/%Y'

# data = datetime(2025, 4, 14)
# data = datetime(2025, 4, 14, 23, 34, 45)
data = datetime.strptime(data_str_data, data_str_fmt)
data_br = datetime.strptime(data_str_data_br, data_str_fmt_br)
print(data)
print(data_br)
