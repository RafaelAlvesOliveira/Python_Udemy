# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a
# expressão inteira será avaliada naquele valor
# são considerados falsy (que já foram vistos)
# 0 0.0 '' False
# Também existe o tipo None que é usado
# para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'

print(True or False)
print(True or False or 0 or 'abc')
print(0 or False or 0 or 'abc' or True)
