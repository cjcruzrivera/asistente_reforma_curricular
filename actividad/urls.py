from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import editar, eliminar
urlpatterns = [
    url(r'^editar', login_required(editar), name='actividad_editar'),
    url(r'^eliminar', login_required(eliminar), name='actividad_eliminar'),

]
