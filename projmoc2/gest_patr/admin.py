from django.contrib import admin
from .models import Bem, Uge, Ugb, Sector, Fornecedor

# Register your models here.
admin.site.register(Bem)
admin.site.register(Uge)
admin.site.register(Ugb)
admin.site.register(Sector)
admin.site.register(Fornecedor)
