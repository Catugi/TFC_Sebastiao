from django.shortcuts import render


def home(request):
    return render(request, "konjevi/home.html")


def cadastrar_produtos(request):
    return render(request, "konjevi/cadastrar_produto.html")


def cadastrar_usuarios(request):
    return render(request, "konjevi/cadastrar_usuario.html")


def efectuar_reserva(request):
    data = {"data": "Mydata"}
    return render(request, "konjevi/efectuar_reserva_quarto.html", data)


def efectuar_vendas(request):
    return render(request, "konjevi/efectuar_venda_.html")