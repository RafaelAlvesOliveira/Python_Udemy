nome = 'Rafael Alves'
altura = 1.80
peso = 84
imc = peso / (altura ** 2)

# "f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura, '
linha_2 = f'pesa {peso} quilos e seu IMC é '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(imc)
