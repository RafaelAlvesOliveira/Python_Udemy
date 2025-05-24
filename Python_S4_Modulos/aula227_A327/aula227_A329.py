# PyPDF2 para manipular arquivos PDF (PdfWriter)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20250502.pdf'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20250502.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

page = reader.pages[0]
imagem = page.images[0]

# writer = PdfWriter()

# with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as arquivo:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(arquivo)

# Esse trecho é para pegar cada uma das páginas do pdf e salvar separadamente.
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore
