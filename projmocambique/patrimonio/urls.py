#urls page for the application
from django.conf.urls import url
from patrimonio import views

#Allows Template tagging
app_name = 'patrimonio'

urlpatterns = [
    url(r'^users/$',views.users,name='users'),
    url(r'^userslist/$',views.userslist,name='userslist'),
]
