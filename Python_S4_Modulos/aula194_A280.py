# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/
# get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
# locale.setlocale(locale.LC_ALL, 'en_SC.UTF-8')
# print(locale.getlocale())

print(calendar.calendar(2025))
print(locale.getlocale())


# Comando para listar todos os locales disponíveis no windows
# for lang in locale.windows_locale.values():
#     print(lang)

# for lang in locale.locale_alias.values():
#     print(lang)
