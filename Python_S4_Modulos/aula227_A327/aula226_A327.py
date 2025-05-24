# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

# type: ignore

import fitz  # PyMuPDF
import io
from pathlib import Path
from PIL import Image

# Configurações de pasta
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20250502.pdf'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20250502.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

# reader = PdfReader(RELATORIO_BACEN)


# 1. Converter páginas para imagens (usando PyMuPDF)
def processar_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)

        # 1. Converter cada página para imagem PNG
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(dpi=200)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            img.save(PASTA_NOVA / f"pagina_{page_num + 1}.png")
            print(f"✅ Página {page_num + 1} convertida para PNG")

            # 2. Extrair imagens embutidas
            extrair_imagens_embutidas(doc, page, page_num)

    except Exception as e:
        print(f"❌ Erro ao processar PDF: {e}")

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

# page0 = reader.pages[0]
# imagem0 = page0.images[0]

# print(page0.extract_text())
# print(len(page0.images[0]))


# Extrai todas as imagens da página
# 2. Extrair imagens embutidas (usando PyMuPDF - método mais confiável)
def extrair_imagens_embutidas(doc, page, page_num):
    try:
        img_list = page.get_images(full=True)
        if not img_list:
            print(f"ℹ️ Página {page_num + 1} não contém imagens embutidas")
            return

        for img_index, img_info in enumerate(img_list):
            xref = img_info[0]
            base_image = doc.extract_image(xref)
            image_data = base_image["image"]

            try:
                img = Image.open(io.BytesIO(image_data))

                # Converter modos problemáticos
                if img.mode == 'PA':
                    img = img.convert('RGBA')
                elif img.mode not in ['RGB', 'RGBA', 'L']:
                    img = img.convert('RGB')

                img.save(
                    PASTA_NOVA / f"pagina_{page_num+1}_img_{img_index}.png")
                print(f"✅ Imagem {img_index} da página {page_num+1} salva")

            except Exception as e:
                print(f"⚠️ Falha ao processar imagem {img_index}: {e}")

    except Exception as e:
        print(f"⚠️ Erro ao extrair imagens da página {page_num + 1}: {e}")


# Processa o PDF
processar_pdf(RELATORIO_BACEN)
