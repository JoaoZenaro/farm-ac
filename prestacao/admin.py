from django.contrib import admin

from .models import Prestacao, Lancamentos, Tipo

# Register your models here.
admin.site.register(Prestacao)
admin.site.register(Lancamentos)
admin.site.register(Tipo)