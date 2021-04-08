from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vendas", views.efectuar_vendas, name="vendas"),
    path("cadastrar_usuarios", views.cadastrar_usuarios, name="cadusuaurio"),
    path("cadastrar_produtos", views.cadastrar_produtos, name="cadproduto"),
    path("efectuar_reserva", views.efectuar_reserva, name="efectuar_reserva"),
    path(
        "cadastrar_fornecedores",
        views.cadastrar_fornecedor,
        name="cadastrar_fornecedores",
    ),
]