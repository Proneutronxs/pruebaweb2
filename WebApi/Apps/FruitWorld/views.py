from tabnanny import check
from django.shortcuts import render, HttpResponse

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Create your views here.

#Páginas en Inglés ----!!!!!
def index(request):
    variable = "Inicio"
    return render(request,'FruitWorld/index.html', {'inicio': variable, 'contacto': variable})


def contact(request):
    if request.GET.get("name"):
        web = "www.fruitworld.com.ar"
        name = request.GET.get("name",0)
        email = request.GET.get("email",1)
        subjet = "Contacto - " + request.GET.get("subjet",2)
        message = "Web: " + web + "\n" +"From: " + name + "\n" + "Contact: " + email + "\n" + "Message: " + request.GET.get("message",3)
        try: 
            msg = MIMEMultipart()
            password = "$2500%Contacto"
            msg['From'] = "contacto@fruitworld.com.ar"
            msg['To'] = "jchambi@zetone.com.ar"
            msg['Subject'] = subjet
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('mail.zetone.com.ar: 587')
            server.starttls()
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()

            print ("Successfully sent email to %s:" % (msg['To']))
            enviado = "enviado"
            variable = "Contacto"
            return render(request,'FruitWorld/sendMessage.html', {'inicio': variable, 'contacto': variable, 'enviado': enviado})

        except Exception as e:
            print("No se pudo envíar")
            print(e)
            enviado = "NOENVIADO"
            variable = "Contacto"
            return render(request,'FruitWorld/sendMessage.html', {'inicio': variable, 'contacto': variable, 'enviado': enviado})
    else:
        variable = "Contacto"
        return render(request,'FruitWorld/contact.html', {'inicio': variable, 'contacto': variable})


#Páginas en Español  ----!!!!!
def spanish(request):
    variable = "Inicio"
    return render(request,'FruitWorld/spanish.html', {'inicio': variable, 'contacto': variable})

def contacto(request):
    if request.GET.get("name"):
        web = "www.fruitworld.com.ar"
        name = request.GET.get("name",0)
        email = request.GET.get("email",1)
        subjet = "Contacto - " + request.GET.get("subjet",2)
        message = "Web: " + web + "\n" +"From: " + name + "\n" + "Contact: " + email + "\n" + "Message: " + request.GET.get("message",3)
        try: 
            msg = MIMEMultipart()
            password = "$2500%Contacto"
            msg['From'] = "contacto@fruitworld.com.ar"
            msg['To'] = "jchambi@zetone.com.ar"
            msg['Subject'] = subjet
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('mail.zetone.com.ar: 587')
            server.starttls()
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()

            print ("Successfully sent email to %s:" % (msg['To']))
            enviado = "enviado"
            variable = "Contacto"
            return render(request,'FruitWorld/envioMensaje.html', {'inicio': variable, 'contacto': variable, 'enviado': enviado})

        except Exception as e:
            print("No se pudo envíar")
            print(e)
            enviado = "NOENVIADO"
            variable = "Contacto"
            return render(request,'FruitWorld/envioMensaje.html', {'inicio': variable, 'contacto': variable, 'enviado': enviado})
    else:
        variable = "Contacto"
        return render(request,'FruitWorld/contacto.html', {'inicio': variable, 'contacto': variable})