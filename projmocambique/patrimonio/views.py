from django.shortcuts import render
from django.http import HttpResponse
# from patrimonio.models import User
from patrimonio.forms import NewUserForm
# Create your views here.

#first page
def index(request):
    return render(request,'patrimonio/index.html')

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'patrimonio/users.html',{'form':form})
