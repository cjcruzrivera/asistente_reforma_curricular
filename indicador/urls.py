from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import IndicadorCreateView, IndicadorUpdateView, eliminar, view_one, actividad

urlpatterns = [
    url(r'^nuevo/(?P<pk>\d+)/$', login_required(IndicadorCreateView.as_view()), name='indicador_crear'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(IndicadorUpdateView.as_view()), name='indicador_editar'),
    url(r'^eliminar/$', login_required(eliminar), name='eliminar'),
    url(r'^actividad/$', login_required(actividad), name='actividad'),
    url(r'^view/(?P<pk>\d+)/$', login_required(view_one), name='view_one'),
    

]
