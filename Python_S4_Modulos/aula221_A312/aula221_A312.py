# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import re
import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1/5000/'

try:
    response = requests.get(url, timeout=5)
    bytes_html = response.content
    parsed_html = BeautifulSoup(
        bytes_html, 'html.parser', from_encoding='utf-8'
    )
    response.raise_for_status()

    # raw_html = response.text
    # parsed_html = BeautifulSoup(raw_html, 'html.parser')

    if parsed_html.title is not None:
        print(parsed_html.title.text)
    else:
        print("Página não possui tag <title>")

    print(f"Status Code: {response.status_code}")
    print(f"Tamanho do conteúdo: {len(response.text)} bytes")

except requests.exceptions.RequestException as e:
    print(f'Falha na conexão: {str(e)}')
    print('Verifique se:')
    print('1. O servidor está rodando no terminal')
    print('2. A porta 5000 está sendo usada')
    print('3. Nenhum firewall está bloqueando')


top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
# print(top_jobs_heading)

if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    print(article)

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())

# print(raw_html)

# Rever as aulas para fazer esse script funcionar, pois não está funcionando
# corretamente.
