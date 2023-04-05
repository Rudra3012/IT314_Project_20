from django.shortcuts import render
from pymongo import MongoClient
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .Classes import User


client = MongoClient('mongodb+srv://Group20:g7uxB5fMdWcstCt4@cluster0.zjgczqo.mongodb.net/?retryWrites=true&w=majority')
db=client['CrossWordManagement']

def SignupPage(request):
    collections = db['crosswordApp_user']
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            new_user = User.User(uname, email, pass1)
            collections.insert_one(new_user.__dict__,)

            return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    collections = db['crosswordApp_user']
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        # user = authenticate(request, username=username, password=pass1)
        reply=collections.find_one({"username": username})
        if reply is not None:
            if reply["password"]==pass1:
                return redirect('home')
            else:
                template = loader.get_template("login.html")
                context ={
                    "fail": True,
                }
                return HttpResponse(template.render(context,request))

    return render(request, 'login.html')


def create_crossword(request):
    return render(request, "create_crossword_automatic.html")


def crossword_list_view(request):
    return render(request, "sample.html")

def create_crossword_automatic(request):
    return render(request, "create_crossword_automatic.html")

def create_crossword_manual(request):
    return render(request, "create_crossword_manual.html")