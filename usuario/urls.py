from django.conf.urls import url

from .views import index, UsuarioCreateView, UsuarioListView, \
    UsuarioUpdateView, UsuarioDeleteView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', UsuarioCreateView.as_view(), name='usuario_crear'),
    url(r'^listar$', UsuarioListView.as_view(), name='usuario_listar'),
    url(r'^editar/(?P<pk>\d+)/$', UsuarioUpdateView.as_view(), name='usuario_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', UsuarioDeleteView.as_view(), name='usuario_eliminar'),
]