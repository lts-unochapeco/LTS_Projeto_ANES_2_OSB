import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def email_com_anexo(remetente_email, senha, destinatario_email,
                          assunto, corpo_mensagem, caminhos_anexos):
    
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente_email
    mensagem["To"] = destinatario_email
    mensagem["Subject"] = assunto
    
    mensagem.attach(MIMEText(corpo_mensagem, "plain"))

    for caminho_anexo in caminhos_anexos:

        nome_arquivo = os.path.basename(caminho_anexo)
    
        try:
            with open(caminho_anexo, "rb") as anexo:
                parte_anexo = MIMEBase("application", "octet-stream")
                parte_anexo.set_payload(anexo.read())
            
            encoders.encode_base64(parte_anexo)
            parte_anexo.add_header("Content-Disposition", f"attachment; filename={nome_arquivo}")
            mensagem.attach(parte_anexo)
        except FileNotFoundError:
            print(f"Erro: O arquivo '{caminho_anexo}' não foi encontrado.")
            return False
        
    texto_mensagem = mensagem.as_string()
    contexto_ssl = ssl.create_default_context()
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto_ssl) as servidor:
            servidor.login(remetente_email, senha)
            servidor.sendmail(remetente_email, destinatario_email, texto_mensagem)
            print("E-mail enviado com sucesso!")
            return True
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")
        return False


def enviando_relatorio_email(caminho_do_arquivo):
    # Email testes: radames@unochapeco.edu.br e cauan.s2005@unochapeco.edu.br
    if caminho_do_arquivo:
        # 4. Preparar as informações para o e-mail
        remetente = "cauan.s2005@unochapeco.edu.br"
        senha_app = "kmgv lagx ypjl zbwm"
        destinatario = "cauan.s2005@unochapeco.edu.br"
        assunto = "Relatório de Editais"
        corpo = "Prezado(a),\n\nEm anexo a planilha atualizada dos editais.\n\nAtenciosamente,\nLTS"
        
        # 5. Enviar o e-mail com o arquivo anexado
        email_com_anexo(remetente, senha_app, destinatario,
                               assunto, corpo, caminho_do_arquivo)
    else:
        print("Não foi possível enviar o e-mail, porque a lista de dados está vazia.")
