from contextvars import Context
from http.client import HTTPResponse
from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from familiares.models import registro_familiar


# Create your views here.
def index(request):
    archivo = open(r"C:\Users\Dell\Documents\Python\Pruebas\MTV_VICTORIA\MTV_VICTORIA\templates\index.html","r")

    contenido_html=archivo.read()
    archivo.close()

    plantilla = Template(contenido_html)
    contexto=Context()
    documento_a_renderizar = plantilla.render(contexto)

    return HttpResponse(documento_a_renderizar)

def lista_familiares_vivana(request):
    familiar = registro_familiar.objects.all()
    return HttpResponse(f"El nombre de mi familiar es {familiar[0].nombre}. Tiene {familiar[0].edad} años y nació el {familiar[0].fecha_nacimiento}. ")

def lista_familiares_horacio(request):
    familiar = registro_familiar.objects.all()
    return HttpResponse(f"El nombre de mi familiar es {familiar[1].nombre}. Tiene {familiar[1].edad} años y nació el {familiar[1].fecha_nacimiento}. ")

def lista_familiares_bianca(request):
    familiar = registro_familiar.objects.all()
    return HttpResponse(f"El nombre de mi familiar es {familiar[2].nombre}. Tiene {familiar[2].edad} años y nació el {familiar[2].fecha_nacimiento}. ")

def lista_familiares_amelia(request):
    familiar = registro_familiar.objects.all()
    return HttpResponse(f"El nombre de mi familiar es {familiar[3].nombre}. Tiene {familiar[3].edad} años y nació el {familiar[3].fecha_nacimiento}. ")
