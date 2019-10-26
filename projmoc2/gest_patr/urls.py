from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.BemListView.as_view(),name='bem_lista'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^bem/(?P<pk>\d+)$', views.BemDetailView.as_view(), name='bem_detalhe'),
    url(r'^bem/new/$', views.CreateBemView.as_view(), name='bem_novo'),
    url(r'^bem/(?P<pk>\d+)/editar/$', views.BemUpdateView.as_view(), name='bem_alterar'),
    url(r'^bem/(?P<pk>\d+)/remover/$', views.BemDeleteView.as_view(), name='bem_remover'),
]