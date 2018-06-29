from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import index, CursoCreateView, CursoListView, CursoUpdateView, CursoDeleteView, PrerrequisitosUpdateView, eliminar, view_one, prerrequisito, detail, eliminar_pre

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(CursoCreateView.as_view()), name='curso_crear'),
    url(r'^listar$', login_required(CursoListView.as_view()), name='curso_listar'),
    url(r'^editar/(?P<pk>\d+)/$',
        login_required(CursoUpdateView.as_view()), name='curso_editar'),
    url(r'^prerrequisitos/(?P<pk>\d+)/$',
        login_required(PrerrequisitosUpdateView.as_view()), name='prerrequisitos_editar'),
    url(r'^eliminar/$', login_required(eliminar), name='eliminar'),
    url(r'^eliminar_pre/$', login_required(eliminar_pre), name='eliminar_pre'),
    url(r'^prerrequisito/$', login_required(prerrequisito), name='prerrequisito'),
    url(r'^detail/$', login_required(detail), name='detail'),
    url(r'^view/(?P<pk>\d+)/$', login_required(view_one), name='view'),
    # url(r'^eliminar/(?P<pk>\d+)/$', login_required(CursoDeleteView.as_view()), name='curso_eliminar'),
]
