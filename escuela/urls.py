from django.conf.urls import url

from .views import index, EscuelaCreateView, EscuelaListView, EscuelaUpdateView, EscuelaDeleteView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', EscuelaCreateView.as_view(), name='escuela_crear'),
    url(r'^listar$', EscuelaListView.as_view(), name='escuela_listar'),
    url(r'^editar/(?P<pk>\d+)/$', EscuelaUpdateView.as_view(), name='escuela_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', EscuelaDeleteView.as_view(), name='escuela_eliminar'),
]