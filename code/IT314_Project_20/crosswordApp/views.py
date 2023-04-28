from bson import ObjectId
from django.contrib import messages
from django.shortcuts import render
# from pymongo import MongoClient
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from .Classes import User
from .helper import send_mail


import uuid
# client = MongoClient('mongodb+srv://Group20:g7uxB5fMdWcstCt4@cluster0.zjgczqo.mongodb.net/?retryWrites=true&w=majority')

from pymongo.mongo_client import MongoClient

# Create a new client and connect to the server
client = MongoClient("mongodb+srv://Group20:Group20@cluster0.vl47pk0.mongodb.net/?retryWrites=true&w=majority")
db = client['CrossWordManagement']


def SignupPage(request):
    collections = db['crosswordApp_user']
    template = loader.get_template("signup.html")

    context = {
    }

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')


        if pass1 != pass2:
            print("Passwords do not match")
            context['displayMessage'] = True
            context['message_type'] = 'errorMessage'
            context['message_content'] = "Passwords do not match"
            return render(request, "signup.html", context)
        else:


            new_user = User.User(uname, email, pass1)

            context['displayMessage'] = False

            if not new_user.check_username():
                context['displayMessage'] = True
                print("Username is invalid")
                context['message_type'] = 'errorMessage'
                context['message_content'] = new_user.message
                return render(request, "signup.html", context)

            print("Username is valid")

            if not new_user.check_email():
                print("Email is invalid")
                context['displayMessage'] = True
                context['message_type'] = 'errorMessage'
                context['message_content'] = new_user.message
                return render(request, "signup.html", context)

            print("Email is valid")

            if not new_user.check_password():
                context['displayMessage'] = True
                context['message_type'] = 'errorMessage'
                context['message_content'] = new_user.message
                return render(request, "signup.html", context)

            print("Password is valid")

            collections.insert_one(new_user.__dict__)

            db['crosswordApp_Subscribers'].insert_one({"username": uname, "followers": [], "following": []})

            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

    collections = db['crosswordApp_user']
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        # user = authenticate(request, username=username, password=pass1)

        if username=='admin' and pass1=='admin':
            request.session['username'] = username
            return redirect('/admin')

        redirect_url = request.session.get('redirectTo')

        if redirect_url is None:
            redirect_url = "/home"

        reply = collections.find_one({"username": username})

        print("redirect_url is ", redirect_url)
        if reply is not None:
            # print("reply is not nones")
            if reply["password"] == pass1:
                print("Login Successful")
                request.session['username'] = username
                if redirect_url is not None:
                    print("username saved is ", request.session.get('username') )
                    request.session['redirectTo'] = None
                    return redirect(redirect_url)
                return redirect('/home')
            else:
                print("Password is incorrect")
                print("redirect_url is ", request.session.get('redirectTo'))
                template = loader.get_template("login.html")
                context = {
                    "fail": True,
                    "redirect_url": redirect_url,
                }
                return render(request, 'login.html', context)
        else:
            template = loader.get_template("login.html")
            context = {
                "fail": True,
                "redirect_url": redirect_url,
            }
            return HttpResponse(template.render(context, request))

    return render(request, 'login.html')


def create_crossword(request):
    username = request.session.get('username')
    print("Current User in browsing page: ", username)
    if username is None:
        context = {
            "displayMessage": "yes",
            "message_content": "Please login to solve crosswords ",
            "message_type": "errorMessage",
        }
        request.session['redirectTo'] = '/create_crossword_automatic'
        return render(request, "login.html", context)
        # return redirect('login')

    return render(request, "create_crossword_automatic.html")


def crossword_list_view(request):
    return render(request, "sample.html")


def create_crossword_automatic(request):
    user = request.session.get('username')
    # username = request.session.get('username')
    print("Current User in browsing page: ", user)
    if user is None:
        context = {
            "displayMessage": "yes",
            "message_content": "Please login to create crosswords ",
            "message_type": "errorMessage",
        }
        request.session['redirectTo'] = '/create_crossword_automatic/'
        return render(request, "login.html", context)

    print("Current User: ", user)

    context = {
        "Username": user,
    }
    return render(request, "create_crossword_automatic.html", context)


def create_crossword_manual(request):
    user = request.session.get('username')
    print("Current User in browsing page: ", user)
    if user is None:
        context = {
            "displayMessage": "yes",
            "message_content": "Please login to create crosswords ",
            "message_type": "errorMessage",
        }
        request.session['redirectTo'] = '/create_crossword_manual/'
        return render(request, "login.html", context)
    context = {
        "Username": user,
    }
    return render(request, "create_crossword_manual.html", context)


def creation(request):
    return render(request, "creation.html")


def home(request):
    print(request.session.get('username'))

    userpresent = True

    if request.session.get('username') is None:
        userpresent = False

    context = {
        "username": request.session.get('username'),
        "userPresent": userpresent,
    }
    print("context is ", context)
    return HttpResponse(render(request, "home.html", context))


def logout(request):
    request.session.flush()
    context = {
        "username": None,
        "userpresent": False,
    }
    return redirect('/home')
    # return HttpResponse(render(request, "home.html", context))


def creatorProfile(request):
    return render(request, "creatorProfile.html")


def adminPage(request):
    if request.session.get('username')!= 'admin':
        return HttpResponse("<h1>Access Denied</h1>You are not authorized to view this page")
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

    collections = db['crosswordApp_crossword']

    crosswords = collections.find({})

    crosswords = list(crosswords)

    for crossword in crosswords:
        crossword['crossword_id'] = str(ObjectId(crossword['_id']))
        print(crossword['crossword_id'])
    print(crosswords)

    context = {
        "crosswords": crosswords,
    }

    return render(request, "Admin/crosswordlist.html", context)


def AdminModifyCrosswordPage(request):
    return render(request, "Admin/modify_crossword.html")

def ProcessModifyCrosswordRequest(request, crossword_id):

    collections = db['crosswordApp_crossword']

    collections.delete_one({"_id": ObjectId(crossword_id)   })

    reply = collections.find_one({"_id": ObjectId(crossword_id)})

    return redirect('/admin/crosswordList')


def ProcessModifyUserRequest(request, username):
    print('Processing Modify User Request for user: ', username)

    collections = db['crosswordApp_user']
    reply = collections.find_one({"username": username})
    if request.method == 'POST':
        nemail = request.POST.get('new_email')

        collections.update_one({"username": username}, {"$set": {"email": nemail}})

        return redirect('/admin/userList')

    print(reply)
    if reply is not None:
        context = {
            "user": reply,
        }
        return render(request, f"Admin/modify_user.html", context)

    return render(request, f"Admin/modify_user.html")


def DeleteModifyUserRequest(request, username):

    print('Processing Delete User Request for user: ', username)

    collections = db['crosswordApp_user']

    collections.delete_one({"username": username})

    return redirect('/admin/userList')


def forget_password(request):
    collections = db['crosswordApp_user']
    if request.method == 'POST':
        email = request.POST.get('email')
        reply = collections.find_one({"email": email})
        if reply is not None:
            token = str(uuid.uuid4())
            subject = 'Your forget password link'
            mssg = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/{email}/'
            send_mail(email, subject, mssg)
            messages.success(request, 'An email is sent.')
            return redirect("/forget_password/")

    return render(request, 'forget_password.html')


def ChangePassword(request, token, email):
    collections = db['crosswordApp_user']

    if request.method == 'POST':
        pass1 = request.POST.get('new_password')
        pass2 = request.POST.get('reconfirm_password')
        if pass1 != pass2:
            messages.success(request, 'both should  be equal.')
            return redirect(f'/change-password/{token}/{email}/')
        # rely = collections.find_one({"email":email})
        prev = {"email": email}
        nexxt = {"$set": {"password": pass1}}
        collections.update_one(prev, nexxt)
        return redirect('login')

    return render(request, 'change-password.html')


def changeDetails(request, username, email):
    collections = db['crosswordApp_user']
    if request.method == 'POST':
        changename = request.POST.get('new_username')
        changeemail = request.POST.get('new_email')
        prev = {"email": email}
        nexxt = {"$set": {"email": changeemail}}
        collections.update_one(prev, nexxt)
        prev1 = {"username": username}
        nexxt1 = {"$set": {"username": changename}}
        collections.update_one(prev1, nexxt1)
        return redirect('login')

    return render(request, f"Admin/modify_user.html")


def crossword_browsing(request):
    username = request.session.get('username')
    print("Current User in browsing page: ", username)
    if username is None:
        context = {
            "displayMessage": "yes",
            "message_content": "Please login to solve crosswords ",
            "message_type": "errorMessage",
        }
        request.session['redirectTo'] = '/crossword_browsing'
        return render(request, "login.html", context)
        # return redirect('login')

    if request.method == 'POST':
        filter_type = request.POST.get('filterType', None)
        filter_order= request.POST.get('order', None)
        client = MongoClient("mongodb+srv://Group20:Group20@cluster0.vl47pk0.mongodb.net/?retryWrites=true&w=majority")
        db = client['CrossWordManagement']
        collection = db['crosswordApp_crossword']

        print("filter type: ", filter_type)
        print("filter order: ", filter_order)
        sortedPuzzles = []

        if filter_type == 'rating':
             if filter_order == 'asc':
                 sortedPuzzles = collection.find().sort('rating', 1)
             else:
                    sortedPuzzles = collection.find().sort('rating', -1)
        elif filter_type == 'numTimesSolved':
            if filter_order == 'asc':
                sortedPuzzles = collection.find().sort('timesSolved', 1)
            else:
                sortedPuzzles = collection.find().sort('timesSolved', -1)
        elif filter_type == 'avgTimeTaken':
            if filter_order == 'asc':
                sortedPuzzles = collection.find().sort('avgTime', 1)
            else:
                sortedPuzzles = collection.find().sort('avgTime', -1)
        else:
            pass

        puzzles = list(sortedPuzzles)
        for p in puzzles:
            print(p)
        for i in puzzles:
            i['id'] = str(ObjectId(i['_id']))

            i['rating'] = round(i['rating'], 2)
            i['avgTime'] = round(i['avgTime'], 2)
            # print(type(i['avgTime']))
            if i['avgTime'] == 0:
                i['avgTime'] = 'Not solved yet'
            if i['rating'] == 0:
                i['rating'] = 'Not rated yet'


        context = {'puzzles': puzzles,
                   'userPresent': True,
                   'username': username,
        }
        print("context: ", context)
        return render(request, 'crossword_browsing.html', context)
        # return render(request, 'crossword_browsing.html', {'puzzles': puzzles})
    else:
        client = MongoClient("mongodb+srv://Group20:Group20@cluster0.vl47pk0.mongodb.net/?retryWrites=true&w=majority")
        db = client['CrossWordManagement']
        collection = db['crosswordApp_crossword']
        puzzles = collection.find()
        puzzles = list(puzzles)

        for i in puzzles:
            i['id'] = str(ObjectId(i['_id']))
            i['rating'] = round(i['rating'], 2)
            i['avgTime'] = round(i['avgTime'], 2)
            # print(type(i['avgTime']))
            if i['avgTime'] == 0:
                i['avgTime'] = 'Not solved yet'
            if i['rating'] == 0:
                i['rating'] = 'Not rated yet'

        context = {'puzzles': puzzles,
                   'userPresent': True,
                   'username': username,
        }
        print("context: ", context)
        return render(request, 'crossword_browsing.html', context)


def solve_crossword(request, crossword_id):
    username = request.session.get('username')



    context = {
        'user': username,
        'crossword_id': crossword_id,
    }
    # 6442e9c5401d19b1b87a0c2c
    return render(request, "solveCrossword/solveCrossword.html", context)

# def test_timer(request):
#     return render(request, "test_timer.html")

def delete_user(request, delt):
    collections = db['crosswordApp_user']
    collections.delete_one({"username":delt})
    # return redirect('login')
    return render(request, 'delete_user.html')

def CreatorProfile(request, username):
    print("username: ", username)
    activeUser = request.session.get('username')

    collections = db['crosswordApp_Subscribers']

    context = {
        'username': username,
        'isFollowing': False,
        'followers': 0,
        'following': 0,
    }



    if request.method == 'POST':
        action = request.POST.get('ActionFollow')

        if action=='Follow':
            print(f'{activeUser} wants to follow {username}')
            reply = collections.find({"username":username})
            # reply = list(reply)
            print("reply: ", reply)
            if reply:
                collections.update_one({"username":username}, {"$push":{"followers":activeUser}})
                collections.update_one({"username":activeUser}, {"$push":{"following":username}})

            context['isFollowing'] = True
        else:
            reply = collections.find({"username":username})

            collections.update_one({"username":username}, {"$pull":{"followers":activeUser}})
            collections.update_one({"username":activeUser}, {"$pull":{"following":username}})
            print(f'{activeUser} wants to unfollow {username}')
            context['isFollowing'] = False

        collection_crossword = db['crosswordApp_crossword']

        reply = collection_crossword.find({"creator":username})

    reply_cCreated = list(db["crosswordApp_crossword"].find({"creator":username}))
    reply_cSolved = list(db["solvedCrosswords"].find({"user":username}))
    print("reply_ccreated: ", len(reply_cCreated))
    print("reply_csolved: ", len(reply_cSolved))

    context['crosswordsCreated'] = len(reply_cCreated)
    context['crosswordsSolved'] = len(reply_cSolved)
    context['crosswordsCreatedList'] = reply_cCreated
    context['crosswordsSolvedList'] = reply_cSolved

    reply = list(collections.find({"username":username}))

    context['followers'] = len(reply[0]['followers'])
    context['following'] = len(reply[0]['following'])

    print(context)
    if len(reply)>0:
        if activeUser in reply[0]['followers']:
            print(f'{activeUser} is following {username}')
            context['isFollowing'] = True
    else:
        context['isFollowing'] = False
    return render(request,f"Profile/index.html", context)

def create_auto(request):
    return render(request,"automatic.html")

def tutorial(request):
    return render(request,"Tutorial_page_v3/Tut_main.html")

def tutorial_auto(request):
    return render(request,"Tutorial_page_v3/Tut_auto.html")

def tutorial_manual(request):
    return render(request,"Tutorial_page_v3/Tut_manual.html")

def tutorial_solving(request):
    return render(request,"Tutorial_page_v3/Tut_solver.html")

def daily_puzzle(request):
    return HttpResponse("<h1>Daily Puzzle</h1><h2>Feature Coming Soon</h2>")