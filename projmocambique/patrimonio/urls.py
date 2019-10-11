#urls page for the application
from django.conf.urls import url
from patrimonio import views

urlpatterns = [
    url(r'^$',views.users,name='users'),
]
