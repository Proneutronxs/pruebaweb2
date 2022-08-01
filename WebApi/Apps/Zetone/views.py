from django.shortcuts import render

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Create your views here.

def sendMail():
    try:
        msg = MIMEMultipart()
        message = "Run Send Mail for Python"
        
        password = "ContactoZetone$$2500"
        msg['From'] = "contacto.zetone@zetone.com.ar"
        msg['To'] = "jchambi@zetone.com.ar"
        msg['Subject'] = "Contacto - Web Zetone"
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP('mail.zetone.com.ar: 587')
        
        server.starttls()
        
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        
        print ("Successfully sent email to %s:" % (msg['To']))
    except Exception as e:
        print("No se pudo envíar")
        print(e)