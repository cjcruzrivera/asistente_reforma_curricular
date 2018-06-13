from django.conf.urls import url

from django.contrib.auth.views import login
from .views import carga_datos_inicial

urlpatterns = [
    url(r'^accounts/login/', login, {'template_name':'login.html'} ,name='login') ,   
    url(r'^$', login, {'template_name':'login.html'} ,name='login2') ,   
    url(r'^carga/', carga_datos_inicial ,name='carga') ,   
    ]