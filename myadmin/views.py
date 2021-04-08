from django.shortcuts import render


def login(request):
    return render(request, "myadmin/login.html")


def logout(request):
    return render(request, "myadmin/logout.html")