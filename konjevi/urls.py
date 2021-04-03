from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vendas", views.efectuar_vendas, name="vendas"),
    path("cadastrar_usuarios", views.cadastrar_usuarios, name="cadusuaurio"),
    path("vendas", views.cadastrar_produtos, name="cadproduto"),
    path("vendas", views.efectuar_reserva, name="efectuar_reserva"),
]