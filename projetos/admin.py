from django.contrib import admin
from .models import Projeto


class ProjetoAdm(admin.ModelAdmin):
    pass


admin.site.register(Projeto, ProjetoAdm)
