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
from datetime import datetime
# from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('17/04/2025 08:20:20', fmt)
delta = data_fim - data_inicio
# delta = timedelta(days=10, hours=2)

# relativedelta é usado para fazer comparaçõoes de tempo usando anos, semanas,
# minutos, segundos entre outros.
# delta = relativedelta(data_fim, data_inicio)
# print(delta)
# print(delta.days, delta.years)
# print(data_fim + delta)

# Dateutil serve para criar um timedelta relativo, pois é possível acrescentar
# valores que não seriam permitidos no timedelta.
print(data_fim)
print(data_fim + relativedelta(seconds=60, minutes=10))

# O time delta pode retornar a difereneça entre duas datas na quantidade de
# dias, segundos e microsegundos
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())

# Cálcul de diferença entre datas
# print(data_fim - data_inicio)

# Comparações entre as datas informadas.
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)
