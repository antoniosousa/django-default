from django.shortcuts import render
from rest_framework import viewsets

from .models import Projeto
from .serializers import ProjetoSerializer


class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


def inicio(request):
    projetos = Projeto.objects.all()
    contexto = {"projetos": projetos}
    return render(request, "projetos/inicio.html", contexto)


def detalhe(request, pk):
    projeto = Projeto.objects.filter(id=pk).first()
    contexto = {"projeto": projeto}
    return render(request, "projetos/detalhe.html", contexto)
