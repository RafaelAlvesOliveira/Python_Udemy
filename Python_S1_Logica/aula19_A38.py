primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# primeiro_valor = int(primeiro_valor)
# segundo_valor = int(segundo_valor)

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor é {primeiro_valor}, e é maior que o segundo')
elif primeiro_valor < segundo_valor:
    print(f'O segundo valor é {segundo_valor}, e é maior que o primeiro')
else:
    print(f'O primeiro {primeiro_valor}, e segundo {segundo_valor} são iguais')
