from django.conf.urls import url

from usuario.views import index

urlpatterns = [
    url(r'^$', index),
]