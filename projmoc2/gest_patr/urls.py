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
]
