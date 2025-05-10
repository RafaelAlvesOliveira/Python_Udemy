# Enviando E-mails SMTP com Python
# Continuação - Aula 303
import os
import pathlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from html import escape
import smtplib
import ssl

from dotenv import load_dotenv   # type: ignore

load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula214_A303.html'


# Importar o SSL
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.minimum_version = ssl.TLSVersion.TLSv1_2  # Força TLS 1.2+


# Leitura do arquivo HTML com tratamento robusto de encoding
def load_html_template(file_path):
    encodings = ['utf-8', 'latin-1', 'utf-16']  # Ordem de tentativas
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return Template(f.read())
        except UnicodeDecodeError:
            continue
    raise ValueError(
        f"Não foi possível ler o arquivo {file_path} com os encodings testados"
    )

# Dados do remetente e destinatátio
# remetente = os.getenv('FROM_EMAIL', '')
# destinatario = remetente


# Configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 465
# smtp_port_tls = 587   # STARTTLS
# smtp_username = os.getenv('FROM_EMAIL', '')
# smtp_password = os.getenv('EMAIL_PASSWORD', '')

smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')
smtp_destination = os.getenv('FROM_EMAIL_DESTINATARIO', '')

# email_from = os.getenv('FROM_EMAIL', '')
# password = os.getenv('EMAIL_PASSWORD', '')
# email_to = os.getenv('FROM_EMAIL_DESTINATARIO', '')

# Mensagem de texto
try:
    with open(CAMINHO_HTML, 'r') as arquivo:
        texto_arquivo = arquivo.read()
        template = Template(texto_arquivo)
        texto_email = template.substitute(nome=escape('João'))
except FileNotFoundError:
    print(f"Erro: Arquivo {CAMINHO_HTML} não encontrado.")
    exit()
except Exception as e:
    print(f"Erro ao ler o arquivo HTML: {e}")
    exit()

# Transformar nossa mensagem em MIMEMultipart
msg = MIMEMultipart('alternative')
msg['From'] = smtp_username
msg['To'] = smtp_destination
msg['Subject'] = "Assunto do e-mail"

msg.attach(MIMEText("Seu cliente de e-mail não suporta HTML", 'plain'))
msg.attach(MIMEText(texto_arquivo, 'html'))

# mime_multipart = MIMEMultipart()
# mime_multipart['from'] = remetente
# mime_multipart['to'] = destinatario
# mime_multipart['subject'] = 'Este é oi assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
# mime_multipart.attach(corpo_email)

# Envia o e-mail
# try:
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server = smtplib.SMTP_SSL(smtp_server, smtp_port)
#         server.ehlo()
#         server.starttls()
#         server.login(email_from, password)
#         # server.login(smtp_username, smtp_password)
#         server.sendmail(email_from, email_to, msg.as_string())
#         # server.send_message(mime_multipart)
#         server.quit()
#         print('E-mail enviado com sucesso!')
# except Exception as e:
#     print(f'Erro ao enviar e-mail: {e}')
# finally:
#     server.quit()

# Continuação Teste
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, smtp_destination, msg.as_string())
        print('✅ E-mail enviado com sucesso!')
except smtplib.SMTPAuthenticationError:
    print('❌ Falha na autenticação: verifique e-mail e senha/App Password')
except smtplib.SMTPServerDisconnected:
    print('❌ Conexão com o servidor perdida: verifique rede/firewall')
except Exception as e:
    print(f'❌ Erro ao enviar e-mail: {e}')
