# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

# Calendário completo
# print(calendar.calendar(2025))

# Calendário do mês informado
# print(calendar.month(2025, 4))

# Enumera os dias da semana
# 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursady, 4 = Friday,
# 5 = Saturday, 6 = Sunday
# print(list(enumerate(calendar.day_name)))

# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2025, 12)

# Informação do nome da semana do primeiro dia do mês informado.
# print(calendar.day_name[numero_primeiro_dia])

# Informação do nome do último dia do mês informado.
# print(calendar.day_name[calendar.weekday(2025, 12, ultimo_dia)])

# Informa o número do dia de acordo com os dias da semana.
# print(calendar.weekday(2025, 12, ultimo_dia))

# Represnetação da semana em dias.
# print(calendar.monthcalendar(2025, 12))
for week in calendar.monthcalendar(2025, 12):
    # Enumerando os dias da semana com enumerate
    # print(list(enumerate(week)))
    for day in week:
        if day == 0:
            continue
        print(day)
