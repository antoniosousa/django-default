from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpRequest

# Create your views here.
def inicio(request: HttpRequest) -> HttpResponse:
    return render(request, "projetos/inicio.html")