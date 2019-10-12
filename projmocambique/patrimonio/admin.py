from django.contrib import admin
from patrimonio.models import UserProfileInfo, User
# Register your models here.
admin.site.unregister(User)
admin.site.register(UserProfileInfo)
