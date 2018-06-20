from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import index, UsuarioCreateView, UsuarioListView, \
    UsuarioUpdateView, UsuarioDeleteView, eliminar, consulta_programa, perfil

urlpatterns = [
    url(r'^$', login_required(index), name='index'),
    url(r'^nuevo/$', login_required(UsuarioCreateView.as_view()), name='usuario_crear'),
    url(r'^listar/$',  login_required(UsuarioListView.as_view()), name='usuario_listar'),
    url(r'^editar/(?P<pk>\d+)/$',  login_required(UsuarioUpdateView.as_view()), name='usuario_editar'),
    url(r'^eliminar/$', login_required(eliminar), name='eliminar'),    
    url(r'^perfil/(?P<pk>\d+)/$', login_required(perfil), name='perfil'),    
    url(r'^consulta_programa/$', login_required(consulta_programa), name='eliminar'),    
    # url(r'^eliminar/(?P<pk>\d+)/$',  login_required(UsuarioDeleteView.as_view()), name='usuario_eliminar'),
]