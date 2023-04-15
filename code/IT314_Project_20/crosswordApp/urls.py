"""CrosswordManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from crosswordApp import views

urlpatterns = [
    path("login/", views.LoginPage, name="login"),
    path("signup/",views.SignupPage, name='signup'),
    path("create_crossword/", views.create_crossword, name="create_crossword"),
    path("unicorn/", include("django_unicorn.urls")),
    path("crossword_list_view/", views.crossword_list_view, name="crossword_list_view"),
    path("create_crossword_automatic/", views.create_crossword_automatic, name="create_crossword_automatic"),
    path("create_crossword_manual/", views.create_crossword_manual, name="create_crossword_manual"),
    path("creation", views.creation, name="creation"),
    path("",views.home, name="home"),
    path("logout/", views.logout, name="logout"),
    path("creatorProfile/", views.creatorProfile, name="creatorProfile"),
    path("admin", views.adminPage, name="adminPage"),
    # path("admin/crosswordList/<int:crossword_id>/", views.AdminCrosswordListPage, name="AdminCrosswordListPage"),
    path("admin/crosswordList", views.AdminCrosswordListPage, name="AdminCrosswordListPage"),
    # path("admin/crosswordList/<int:crossword_id>/delete/", views.AdminCrosswordDelete, name="AdminCrosswordDeletePage"),
    path("admin/userList", views.AdminUserListPage, name="AdminUserListPage"),
    # path("admin/userList/<int:user_id>/", views.AdminUserListPage, name="AdminUserListPage"),
    path("admin/modifyUserRequest/<str:username>/", views.ProcessModifyUserRequest, name="ProcessModifyUserRequest"),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('change-password/<token>/<email>/', views.ChangePassword, name="change_password"),
]
