from django.urls import path
from .views import *

urlpatterns = [
    path("", createAccount, name="createAccount"),
    path("login", loginView, name="login"),
    path("logout", logoutView, name="logout"),

    path("register", registerView, name="register"),
    path("school_register", schoolRegView, name="schoolRegView"),
    path("school/", profile, name="Profile"),

]
