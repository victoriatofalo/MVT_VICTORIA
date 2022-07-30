"""MTV_VICTORIA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from familiares.views import lista_familiares_vivana,lista_familiares_horacio,lista_familiares_bianca,lista_familiares_amelia,index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Viviana/', lista_familiares_vivana),
    path('Horacio/', lista_familiares_horacio),
    path('Bianca/', lista_familiares_bianca),
    path('Amelia/', lista_familiares_amelia),
    path('',index)
]
