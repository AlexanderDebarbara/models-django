from django.conf.urls import url
from . import views

app_name = 'pessoa'
urlpatterns = [
    url(r'^$', views.PessoaLista.as_view(), name = 'pessoa_list'),
    url(r'^add/$', views.PessoaAdd.as_view(), name = 'pessoa_new'),
    url(r'^edit/(?P<pk>\d+)$',  views.PessoaUpdate.as_view(), name='pessoa_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.PessoaDelete.as_view(), name='pessoa_delete'),    
]