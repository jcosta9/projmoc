from django.shortcuts import render
from django.http import HttpResponse
from patrimonio.models import User
# Create your views here.

#first page
def index(request):
    return render(request,'patrimonio/index.html')

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    #links db content with static file
    return render(request,'patrimonio/users.html',context=user_dict)
