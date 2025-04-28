# os.listdir para navegar em caminhos
# /Users/Rafael/Desktop/EXEMPLO
# C:\Users\Rafael\Desktop\EXEMPLO
# caminho = r'C:\\Users\\Rafael\\Desktop\\EXEMPLO'
import os

caminho = os.path.join(
    '\\Users', 'Rafael Alves', 'Documents',
    'Rafael', 'VScode', 'Python', 'Python_S4_Modulos', 'aula197_A283'
    )
# print(caminho)

# Serão listados todos os diretórios que estiverem dentro de uma
# determinada pasta
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)

    # Verifica se é um diretorio caso não seja um diretório
    # o loop é encerrado.
    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)
