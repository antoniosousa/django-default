from django.urls import URLResolver, include, path
from rest_framework import routers

from projetos.views import ProjetoViewSet, detalhe, inicio

router = routers.DefaultRouter()
router.register(r'api', ProjetoViewSet)

urlpatterns: list[URLResolver] = [
    path("", inicio, name="inicio"),
    path("<int:pk>/", detalhe, name="detalhe"),
    # api
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls

