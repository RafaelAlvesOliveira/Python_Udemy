import importlib

import aula110_A156M

print(aula110_A156M.variavel)

for i in range(10):
    # print(i)
    importlib.reload(aula110_A156M)
    print(i)
    # import  aula110_A156M

# Singleton significado que só pode haver uma
# instância de uma classe exista em todo o programa.

print('Fim')
