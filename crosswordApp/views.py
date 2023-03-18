from django.shortcuts import render

from .models import user


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user.objects.create(username=username, password=password, email=email)
    print(request.POST.get("username"))

    return render(request, "login.html")


def create_crossword(request):
    return render(request, "create_crossword.html")
