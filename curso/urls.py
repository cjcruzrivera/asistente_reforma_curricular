from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import index, CursoCreateView, CursoListView, CursoUpdateView, CursoDeleteView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(CursoCreateView.as_view()), name='curso_crear'),
    url(r'^listar$', login_required(CursoListView.as_view()), name='curso_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(CursoUpdateView.as_view()), name='curso_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(CursoDeleteView.as_view()), name='curso_eliminar'),
]