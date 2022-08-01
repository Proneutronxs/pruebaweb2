from django.urls import path
from Apps.FruitWorld import views

urlpatterns = [

    #Páginas en Inglés ----!!!!!
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),


    #Páginas en Español  ----!!!!!
    path('spanish', views.spanish, name="spanish"),
    path('contacto', views.contacto, name="contacto"),
]