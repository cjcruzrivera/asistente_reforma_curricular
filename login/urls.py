from django.conf.urls import url

from django.contrib.auth.views import login

urlpatterns = [
    url(r'^accounts/login/', login, {'template_name':'login.html'} ,name='login') ,   
    url(r'^$', login, {'template_name':'login.html'} ,name='login2') ,   
    ]