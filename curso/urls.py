from django.conf.urls import url

from .views import index, CursoCreateView, CursoListView, CursoUpdateView, CursoDeleteView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', CursoCreateView.as_view(), name='curso_crear'),
    url(r'^listar$', CursoListView.as_view(), name='curso_listar'),
    url(r'^editar/(?P<pk>\d+)/$', CursoUpdateView.as_view(), name='curso_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', CursoDeleteView.as_view(), name='curso_eliminar'),
]