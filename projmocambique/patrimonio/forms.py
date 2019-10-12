from django import forms
from patrimonio.models import User1
from django.contrib.auth.models import User
from patrimonio.models import UserProfileInfo

# Created as an example -- DELETE LATER
class NewUserForm(forms.ModelForm):
    class Meta():
        model = User1
        fields = '__all__'



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
