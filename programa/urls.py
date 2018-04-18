from django.conf.urls import url

from .views import index, ProgramaCreateView, ProgramaListView, ProgramaUpdateView, ProgramaDeleteView

urlpatterns = [
	url(r'^$', index, name ='index'),
	url(r'^nuevo$', ProgramaCreateView.as_view(), name='programa_crear'),
    	url(r'^listar$', ProgramaListView.as_view(), name='programa_listar'),
    	url(r'^editar/(?P<pk>\d+)/$', ProgramaUpdateView.as_view(), name='programa_editar'),
    	url(r'^eliminar/(?P<pk>\d+)/$', ProgramaDeleteView.as_view(), name='programa_eliminar'),
]
