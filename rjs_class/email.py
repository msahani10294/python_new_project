import smtplib, ssl

smtl_server = "smtp.gmail.com"
port = 587
sender_mail = "msahani10294@gmail.com"
password = input("enter your password")

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtl_server, port)
    server.ehlo()

    server.starttls(context) # secure your connecion
    server.ehlo()
    server.login(sender_mail, password)
except Exception as e:
    print(e)

finally:
    server.quit()