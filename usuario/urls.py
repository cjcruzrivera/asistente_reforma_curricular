from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import index, UsuarioCreateView, UsuarioListView, \
    UsuarioUpdateView, UsuarioDeleteView

urlpatterns = [
    url(r'^$', login_required(index), name='index'),
    url(r'^nuevo$', login_required(UsuarioCreateView.as_view()), name='usuario_crear'),
    url(r'^listar$',  login_required(UsuarioListView.as_view()), name='usuario_listar'),
    url(r'^editar/(?P<pk>\d+)/$',  login_required(UsuarioUpdateView.as_view()), name='usuario_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',  login_required(UsuarioDeleteView.as_view()), name='usuario_eliminar'),
]