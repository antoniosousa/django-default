from django.urls import path, URLResolver
from paginas import views

urlpatterns: list[URLResolver] = [
    path("", views.inicio, name='inicio'),
]