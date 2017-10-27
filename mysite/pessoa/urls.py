from django.conf.urls import url
from . import views 

app_name = 'pessoa'
urlpatterns = [
    url(r'^$', views.PessoaLista.as_view(), name = 'pessoa_list'),
    url(r'^add/$', views.pessoa_new, name = 'pessoa_new'),
    url(r'^edit/(?P<pk>\d+)$',  views.PessoaUpdate.as_view(), name='pessoa_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.PessoaDelete.as_view(), name='pessoa_delete'),
    url(r'^endereco_add/$', views.EnderecoAdd.as_view(), name = 'endereco_new'),
    url(r'^prontuario/$', views.ProntuarioList.as_view(), name = 'pronturario_list'),
    url(r'^prontuario_add/$', views.ProntuarioAdd.as_view(), name = 'prontuario_new'),
]