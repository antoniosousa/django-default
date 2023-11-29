from django.urls import path, URLResolver
from projetos import views

urlpatterns: list[URLResolver] = [
    path("", views.inicio, name='inicio'),
]