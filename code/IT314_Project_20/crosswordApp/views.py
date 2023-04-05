from django.shortcuts import render
from pymongo import MongoClient
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .Classes import User

client = MongoClient('mongodb+srv://Group20:g7uxB5fMdWcstCt4@cluster0.zjgczqo.mongodb.net/?retryWrites=true&w=majority')
db=client['CrossWordManagement']

def login(request):
    collections = db['crosswordApp_user']
    validate = "success"
    template = loader.get_template('login.html')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # new_user = User.User(username, password, email)
        # collections.insert_one(new_user.__dict__)
        # print(new_user)
        reply=collections.find_one({"username": username})
        print(f'Record found for {username}', reply)
        if reply is None:
            print("User not found")
            return render(request, "login.html")
        else:
            print("User found")
            if reply["password"] == password:
                return render(request, "create_crossword_manual.html")
            else:
                validate="fail"
                print("Password incorrect")

    print(request.POST.get("username"))
    context ={
        "Reply": validate,
    }
    return HttpResponse(template.render(context, request))


def create_crossword(request):
    return render(request, "create_crossword_automatic.html")


def crossword_list_view(request):
    return render(request, "sample.html")

def create_crossword_automatic(request):
    return render(request, "create_crossword_automatic.html")

def create_crossword_manual(request):
    return render(request, "create_crossword_manual.html")