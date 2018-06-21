from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import ResultadoAprendizajeCreateView, ResultadoAprendizajeUpdateView, eliminar, view_one, actividad
urlpatterns = [
    url(r'^nuevo/(?P<pk>\d+)/$', login_required(ResultadoAprendizajeCreateView.as_view()), name='resultadoAprendizaje_crear'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(ResultadoAprendizajeUpdateView.as_view()), name='resultadoAprendizaje_editar'),
    url(r'^eliminar/$', login_required(eliminar), name='eliminar'),
    url(r'^view/(?P<pk>\d+)/$', login_required(view_one), name='view_one'),
    url(r'^actividad/$', login_required(actividad), name='actividad'),

]
