from django.urls import path
from .views import valor_total_estoque

urlpatterns = [
    path('valor-total/', valor_total_estoque, name='valor_total_estoque'),
]
