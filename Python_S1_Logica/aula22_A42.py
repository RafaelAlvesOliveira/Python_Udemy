# Operadores lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha:')

# if senha != '123456':
#     print('Senha incorreta.')

if not senha:
    print('Você não digitou nada')

print(not 0)  # True
print(not 1)  # False

print(not True)  # False
print(not False)  # True
