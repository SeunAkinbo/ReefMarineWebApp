import smtplib
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from string import Template


receiver_email = 'seunakinbo@gmail.com'
message = 'Subject: Welcome Onboard\n\nHello,\nWe are glad to welcome you on board with us.\nWe assure of premium service.\nRegards'


def send_multiformat_mail(receiver_email, html_format_mssg, message):
    port = 465
    smtp_server = 'smtp.gmail.com'
    sender_email = 'barry.white.23409'
    password = 'barrywhite23409'

    # Creates the email content, which is an object of the MIMEMultipart
    email = MIMEMultipart("alternative")
    email['from'] = sender_email
    email['to'] = receiver_email
    email['subject'] = 'Reef Marine - Contact Mail Copy'

    # Create the MIMEText for both HTML & Text format
    # html_mssg = Template(Path('Templates/mail.html').read_text())

    text_format = MIMEMultipart(message, 'plain')
    html_format = MIMEMultipart(html_format_mssg, 'html')

    email.attach(text_format)
    email.attach(html_format)

    # Create context to validate the hostname, certificates and secure the connection
    context = ssl.create_default_context()

    # Establish a connection with the mail server using a secured ssl and encrypting with a tls
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as mail_server:
        mail_server.login(sender_email, password)
        mail_server.send_message(email)


def send_mail(receiver_email, message):
    port = 465
    smtp_server = 'smtp.gmail.com'
    password = 'barrywhite23409'
    sender_email = 'barry.white.23409'

    # Create HTML content
    # html = Template(Path('Templates/mail.html').read_text())
    # email.set_content(html.substitute({'message':message}), 'html')

    # Creates the email content, which is an object of the EmailMessage
    email = EmailMessage()
    email['from'] = sender_email
    email['to'] = receiver_email
    email['subject'] = 'Reef Marine - Contact Mail Copy'
    email.set_content(message)

    # Create context to validate the hostname, certificates and secure the connection
    context = ssl.create_default_context()

    # Establish a connection with the mail server using a secured ssl and encrypting with a tls
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as mail_server:
        mail_server.login(sender_email, password)
        mail_server.send_message(email)


'''
Another way to Implement the mailing client is by creating an unsecure connection using the
smtplib's SMTP function, then .ehlo() to identify with the server, before securing with the
.starttls(context=). The .ehlo() function is declared for use by the .starttls() or .sendmail() 
function as the case maybe. Then login to the server connection using .login(email=, password=)
then you can send your mail using .sendmail() function. Finally we close the server using 
.quit() function.

with smtplib.SMTP(server_name, port) as mail_server
    mail_server.ehlo()
    mail_server.starttls(context=context)
    mail_server.login(sender_email, password)
    mail_server.send_message(email)
'''
