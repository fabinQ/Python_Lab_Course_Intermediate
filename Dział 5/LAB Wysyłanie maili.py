import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Definiujemy port i serwer smtp poczty
port = 465
smtp_server = "smtp.gmail.com"



# Definiujemy dane: nazwa, mail z którego wysyłamy, hasło do poczty, temat i do kogo chcemy wysłać
mailFrom = "Maciej Fabiński"
user = 'maciejfabinski@gmail.com'
password = 'bovwxoxglprvppzb'
mailSubject = "HTML mail test"
mailTo = ['maciejfabinski@gmail.com']


# Treść HTML wiadomości - ją się dodaje jest tak jakby osobno. Jeśli piszemy bez html to przy dodawaniu treści trzeba wpisać .attacht(MIMEText(mailBody, "plain"))
mailBody = """
<html>
    <body>
		<h1>Nicpoń</h1>
        <p>Teraz mail z POLSKIMI znakami ąęćńżźół</p>
        <p>oraz HTML</p>
        <b>LOFKI :*</b>
    </body>
</html>
"""



# Tworzenie wiadomości MIME - MIMEMultipart jest bardziej złożoną klasą w niej dodajemy odbiorców itd. mozna także dodać załączniki.
# W naszym przypadku dodajemy załącznik MIMEText z obiektem "HTML" i kodowaniem.
message = MIMEMultipart("alternative")
message["Subject"] = mailSubject
message["From"] = mailFrom
message["To"] = ", ".join(mailTo)

# Dodanie treści HTML wiadomości z poprawnym kodowaniem
htmlPart = MIMEText(mailBody, "html", "utf-8")
message.attach(htmlPart)


try:
    ssl_ctx = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server, port, context=ssl_ctx)
    server.ehlo()
    server.login(user, password)
    server.sendmail(message["From"], message["To"], message.as_string())
    server.close()
    print("mail sent")
except:
    print("Something wrong.")