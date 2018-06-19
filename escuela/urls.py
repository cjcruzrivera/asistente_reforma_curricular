from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import index, EscuelaCreateView, EscuelaListView, EscuelaUpdateView, eliminar, view_one

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(EscuelaCreateView.as_view()), name='escuela_crear'),
    url(r'^listar$', login_required(EscuelaListView.as_view()), name='escuela_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(EscuelaUpdateView.as_view()), name='escuela_editar'),
    url(r'^eliminar/$', eliminar, name='eliminar'),
    url(r'^view/(?P<pk>\d+)/$', view_one, name='view_one'),
    # url(r'^eliminar/(?P<pk>\d+)/$', login_required(EscuelaDeleteView.as_view()), name='escuela_eliminar'),
]