from django.conf.urls import url
from gestao_patrimonio import views

url = [
    url(r'^$', views.ListaBensMoveisView.as_view(), name='BensMoveisLista') #home page
    url(r'^about/',views.AboutView.as_view(), name="about"),
    url(r'^bemmovel/(?P<pk>\d+)$', views.BemMovelDetalheView.as_view(), name='bemmovel_detalhe'),
    url(r'^bemmovel/novo/$', views.BemMovelCriarView.as_view(), name='bemmovel_novo'),
    url(r'^bemmovel/(?P<pk>\d+)/atualizar/$', views.BemMovelAtualizarView.as_view(), name='bemmovel_atualizar'),
    url(r'^bemmovel/(?P<pk>\d+)/remover/$', views.BemMovelDeleteView.as_view(), name='bemmovel_remover'),
]
