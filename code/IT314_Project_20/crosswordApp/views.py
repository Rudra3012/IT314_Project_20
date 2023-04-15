from django.shortcuts import render
from pymongo import MongoClient
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .Classes import User

client = MongoClient('mongodb+srv://Group20:Group20@cluster0.fi05hgc.mongodb.net/test')
db = client['CrossWordManagement']


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
            collections.insert_one(new_user.__dict__, )

            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    collections = db['crosswordApp_user']
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        # user = authenticate(request, username=username, password=pass1)
        reply = collections.find_one({"username": username})
        if reply is not None:
            if reply["password"] == pass1:
                request.session['username'] = username
                return redirect('home')
            else:
                template = loader.get_template("login.html")
                context = {
                    "fail": True,
                }
                return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template("login.html")
            context = {
                "fail": True,
            }
            return HttpResponse(template.render(context, request))
    return render(request, 'login.html')


def create_crossword(request):
    return render(request, "create_crossword_automatic.html")


def crossword_list_view(request):
    return render(request, "sample.html")


def create_crossword_automatic(request):
    return render(request, "create_crossword_automatic.html")


def create_crossword_manual(request):
    return render(request, "create_crossword_manual.html")


def creation(request):
    return render(request, "creation.html")


def home(request):
    print(request.session.get('username'))

    userpresent = True

    if request.session.get('username') is None:
        userpresent = False

    context = {
        "username": request.session.get('username'),
        "userpresent": userpresent,
    }
    return HttpResponse(render(request, "home.html", context))


def logout(request):
    request.session.flush()
    context = {
        "username": None,
        "userpresent": False,
    }
    # redirect('')
    return HttpResponse(render(request, "home.html", context))


def creatorProfile(request):
    return render(request, "creatorProfile.html")


def adminPage(request):
    return render(request, "Admin/admin.html")


def AdminUserListPage(request):
    users = db['crosswordApp_user'].find({})

    users = list(users)
    print(users)
    context = {
        "Users": users,
    }
    return render(request, "Admin/userlist.html", context)


def AdminCrosswordListPage(request):
    return render(request, "Admin/crosswordlist.html")


def AdminModifyCrosswordPage(request):
    return render(request, "Admin/modify_crossword.html")


def ProcessModifyUserRequest(request, username):

    print('Processing Modify User Request for user: ', username)

    collections = db['crosswordApp_user']

    reply = collections.find_one({"username": username})
    print(reply)
    if reply is not None:
        context = {
            "user": reply,
        }
        return render(request, "Admin/modify_user.html", context)


    return render(request, "Admin/modify_user.html")

def forget_password(request):
    collections = db['crosswordApp_user']
    if request.method == 'POST':
        email = request.POST.get('email')
        reply =  collections.find_one({"email":email})
        if reply is not None:
            token = str(uuid.uuid4())
            subject='Your forget password link'
            mssg = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/'
            send_mail(email, subject, mssg)
            messages.success(request, 'An email is sent.')
            return redirect("/forget_password/")

    return render(request, 'forget_password.html')


def ChangePassword(request, token,email):
    collections = db['crosswordApp_user']

    if request.method == 'POST':
        pass1 = request.POST.get('new_password')
        pass2 = request.POST.get('reconfirm_password')
        if pass1 != pass2:
            messages.success(request, 'both should  be equal.')
            return redirect(f'/change-password/{token}/{email}/')
        # rely = collections.find_one({"email":email})
        prev={"email":email}
        nexxt={"$set":{"password":pass1}}
        collections.update_one(prev,nexxt)
        return redirect('login')

    return render(request, 'change-password.html')

