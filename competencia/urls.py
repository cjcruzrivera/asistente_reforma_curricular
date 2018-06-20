from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CompetenciaListView, CompetenciaCreateView, CompetenciaUpdateView, eliminar, view_one
urlpatterns = [
    url(r'^listar/(?P<pk>\d+)/$', login_required(CompetenciaListView.as_view()), name='competencia_listar'),
    url(r'^nuevo/(?P<pk>\d+)/$', login_required(CompetenciaCreateView.as_view()), name='competencia_crear'),
    url(r'^editar/(?P<course>\d+)/(?P<pk>\d+)/$', login_required(CompetenciaUpdateView.as_view()), name='competencia_editar'),
    url(r'^eliminar/$', login_required(eliminar), name='eliminar'),
    url(r'^view/(?P<pk>\d+)/$', login_required(view_one), name='view_one'),

    # url(r'^$', login_required(ProgramaListView.as_view()), name='index'),
    # url(r'^nuevo$', login_required(ProgramaCreateView.as_view()), name='programa_crear'),
    # url(r'^listar$', login_required(ProgramaListView.as_view()), name='programa_listar'),
    # url(r'^editar/(?P<pk>\d+)/$', login_required(ProgramaUpdateView.as_view()), name='programa_editar'),
    # url(r'^eliminar/$', login_required(eliminar), name='eliminar'),
    # url(r'^lista_dir/$', login_required(listar_dir), name='lista_dir'),
    # url(r'^view/(?P<pk>\d+)/$', login_required(view_one), name='view_one'),
    # url(r'^eliminar/(?P<pk>\d+)/$', login_required(ProgramaDeleteView.as_view()), name='programa_eliminar'),
]