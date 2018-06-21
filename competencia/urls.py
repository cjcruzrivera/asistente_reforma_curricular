from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CompetenciaListView, CompetenciaCreateView, CompetenciaUpdateView, eliminar, view_one
urlpatterns = [
    url(r'^listar/(?P<pk>\d+)/$', login_required(CompetenciaListView.as_view()), name='competencia_listar'),
    url(r'^nuevo/(?P<pk>\d+)/$', login_required(CompetenciaCreateView.as_view()), name='competencia_crear'),
    url(r'^editar/(?P<course>\d+)/(?P<pk>\d+)/$', login_required(CompetenciaUpdateView.as_view()), name='competencia_editar'),
    url(r'^eliminar/$', login_required(eliminar), name='eliminar'),
    url(r'^view/(?P<pk>\d+)/$', login_required(view_one), name='view_one'),

]