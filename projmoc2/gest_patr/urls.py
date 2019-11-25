from django.conf.urls import url
from . import views

app_name = 'gest_partr'

urlpatterns = [
    url(r'^$',views.AboutView.as_view(),name='about'),

    url(r'^bem/lista/$',views.BemListView.as_view(),name='bens_lista'),
    url(r'^bem/(?P<pk>\d+)$', views.BemDetailView.as_view(), name='bem_detalhe'),
    url(r'^bem/new/$', views.CreateBemView.as_view(), name='bem_novo'),
    url(r'^bem/(?P<pk>\d+)/editar/$', views.BemUpdateView.as_view(), name='bem_alterar'),
    url(r'^bem/(?P<pk>\d+)/remover/$', views.BemDeleteView.as_view(), name='bem_remover'),

    url(r'^uge/lista/$',views.UgeListView.as_view(),name='uge_lista'),
    url(r'^uge/(?P<pk>\d+)$', views.UgeDetailView.as_view(), name='uge_detalhe'),
    url(r'^uge/new/$', views.CreateUgeView.as_view(), name='uge_novo'),
    url(r'^uge/(?P<pk>\d+)/editar/$', views.UgeUpdateView.as_view(), name='uge_alterar'),
    url(r'^uge/(?P<pk>\d+)/remover/$', views.UgeDeleteView.as_view(), name='uge_remover'),

    url(r'^ugb/lista/$',views.UgbListView.as_view(),name='ugb_lista'),
    url(r'^ugb/(?P<pk>\d+)$', views.UgbDetailView.as_view(), name='ugb_detalhe'),
    url(r'^ugb/new/$', views.CreateUgbView.as_view(), name='ugb_novo'),
    url(r'^ugb/(?P<pk>\d+)/editar/$', views.UgbUpdateView.as_view(), name='ugb_alterar'),
    url(r'^ugb/(?P<pk>\d+)/remover/$', views.UgbDeleteView.as_view(), name='ugb_remover'),

    url(r'^sector/lista/$',views.SectorListView.as_view(),name='sector_lista'),
    url(r'^sector/(?P<pk>\d+)$', views.SectorDetailView.as_view(), name='sector_detalhe'),
    url(r'^sector/new/$', views.CreateSectorView.as_view(), name='sector_novo'),
    url(r'^sector/(?P<pk>\d+)/editar/$', views.SectorUpdateView.as_view(), name='sector_alterar'),
    url(r'^sector/(?P<pk>\d+)/remover/$', views.SectorDeleteView.as_view(), name='sector_remover'),

    url(r'^fornecedor/lista/$',views.FornecedorListView.as_view(),name='fornecedor_lista'),
    url(r'^fornecedor/(?P<pk>\d+)$', views.FornecedorDetailView.as_view(), name='fornecedor_detalhe'),
    url(r'^fornecedor/new/$', views.CreateFornecedorView.as_view(), name='fornecedor_novo'),
    url(r'^fornecedor/(?P<pk>\d+)/editar/$', views.FornecedorUpdateView.as_view(), name='fornecedor_alterar'),
    url(r'^fornecedor/(?P<pk>\d+)/remover/$', views.FornecedorDeleteView.as_view(), name='fornecedor_remover'),
]
