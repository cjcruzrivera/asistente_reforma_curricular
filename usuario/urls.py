from django.conf.urls import url

from usuario.views import index, UsuarioCreateView, UsuarioListView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', UsuarioCreateView.as_view(), name='usuario_crear'),
    url(r'^listar$', UsuarioListView.as_view(), name='usuario_listar'),
]