# Problemas dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=[]):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


lista1 = []
cliente1 = adiciona_clientes('rafael')
adiciona_clientes('Joana', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)
print(cliente2)

cliente2 = adiciona_clientes('Moreira')
adiciona_clientes('Viviane', cliente2)
print(cliente2)
