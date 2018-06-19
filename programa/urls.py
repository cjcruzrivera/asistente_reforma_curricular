from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import index, ProgramaCreateView, ProgramaListView, \
    ProgramaUpdateView, ProgramaDeleteView, eliminar, listar_dir, view_one

urlpatterns = [
    url(r'^$', login_required(ProgramaListView.as_view()), name='index'),
    url(r'^nuevo$', login_required(ProgramaCreateView.as_view()), name='programa_crear'),
    url(r'^listar$', login_required(ProgramaListView.as_view()), name='programa_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(ProgramaUpdateView.as_view()), name='programa_editar'),
    url(r'^eliminar/$', eliminar, name='eliminar'),
    url(r'^lista_dir/$', listar_dir, name='lista_dir'),
    url(r'^view/(?P<pk>\d+)/$', view_one, name='view_one'),
    # url(r'^eliminar/(?P<pk>\d+)/$', login_required(ProgramaDeleteView.as_view()), name='programa_eliminar'),
]
