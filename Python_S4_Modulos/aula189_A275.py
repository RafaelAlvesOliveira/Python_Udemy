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
# from pytz import timezone

data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1744857967.624383))

# data = datetime.now(timezone('Asia/Tokyo'))
# data = datetime(2025, 4, 16, 23, 43, 30, tzinfo=timezone('Asia/Tokyo'))
# print(data)
