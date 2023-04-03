from django.shortcuts import render

from .models import user
from pymongo import MongoClient

client = MongoClient('mongodb+srv://Group20:Group20@cluster0.fi05hgc.mongodb.net/test?retryWrites=true&w=majority')
db=client['CrossWordManagement']

def login(request):
    collections = db['crosswordApp_user']

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user.objects.create(username=username, password=password, email=email)
        new_user = user(username=username, password=password, email=email)
    print(request.POST.get("username"))

    return render(request, "login.html")


def create_crossword(request):
    return render(request, "create_crossword_automatic.html")


def crossword_list_view(request):
    return render(request, "sample.html")

def create_crossword_automatic(request):
    return render(request, "create_crossword_automatic.html")