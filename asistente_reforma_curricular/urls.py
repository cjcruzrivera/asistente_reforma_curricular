"""asistente_reforma_curricular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout

from login.views import index

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('login.urls', namespace="login")),
    url(r'^usuario/', include('usuario.urls', namespace="usuario")),
    url(r'^programa/', include('programa.urls', namespace="programa")),
    url(r'^escuela/', include('escuela.urls', namespace="escuela")),
    url(r'^curso/', include('curso.urls', namespace="curso")),
    url(r'^competencia/', include('competencia.urls', namespace="competencia")),
    url(r'^resultado/', include('resultado_aprendizaje.urls', namespace="resultado")),
    url(r'^indicador/', include('indicador.urls', namespace="indicador")),
    url(r'^logout/', logout, name="salir", kwargs={'next_page': '/'}),
]
