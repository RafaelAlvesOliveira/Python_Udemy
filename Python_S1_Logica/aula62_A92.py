"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal

# numero_1 = decimal.Decimal(0.1)
# numero_2 = decimal.Decimal(0.7)
# O módulo 'decimal' é usado para se ter uma precisão
# maior dos números, mas isso só acontece em casos muito
# específicos.

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
# Os valores que estão dentro das aspas, permitiram que
# o cálculo seja arredondado sem a necessidade de usar
# outros tipos de formatação

numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 3))
# Arredonda para o valor mais próximo,
# caso, haja zero após o último valor
# númerico o mesmo não aparecerá.
