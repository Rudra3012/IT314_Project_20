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
    path("login/", views.login, name="login"),
    path("create_crossword/", views.create_crossword, name="create_crossword"),
    path("unicorn/", include("django_unicorn.urls")),
    path("crossword_list_view/", views.crossword_list_view, name="crossword_list_view"),
    path("create_crossword_automatic/", views.create_crossword_automatic, name="create_crossword_automatic"),
    path("create_crossword_manual/", views.create_crossword_manual, name="create_crossword_manual"),
]
