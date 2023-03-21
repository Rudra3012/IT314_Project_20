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
    return render(request, "create_crossword_automatic.html")


def crossword_list_view(request):
    return render(request, "sample.html")

def create_crossword_automatic(request):
    return render(request, "create_crossword_automatic.html")