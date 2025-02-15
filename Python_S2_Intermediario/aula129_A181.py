# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virutal, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# VOcê pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env
#
# Comandos:
# python -m venv => usado para criar um ambiente virtual
# gcm python => usado para localizar onde o executável do python
# está localizado
# gcm python -Syntax => mostra o caminho completo de onde o
# executável está.
#
# Lib é a pasta onde se localizam as extensões de terceiros usadas
#
# Ativando e desativando meu ambiente virtual
# Windows: .\venv\Scripts\activate
# Linux e Mac: source venv/bin/activate
# Desativar: deactivate
#
# Como criar ambientes virtuais
# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv venv
#
# Sempre abrir o ambiente virutal, pois tudo o que
# for instalado fora dele fica no python global
# Quando a instalação é feita no ambiente virtual
# as extensões só existem nele. Sempre utilizar o
# instalador pip para extensões do python.
#
# criação de ambiente virtual
# Usando o comando python -m venv venv
# Utilizando requirements.txt
# O comando é pip install -r .\requirements.txt
# Através desse comando é possível reinstalar todas
# as extensões do python que existiam no projeto.
# Sempre usar requiriments.txt para reinstalar todas
# as extensões de uma vez.
