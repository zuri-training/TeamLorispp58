from django.urls import path
from .views import *

urlpatterns = [
    path("", createAccount, name="createAccount"),
    path("login", loginView, name="login"),
    path("register", registerView, name="register"),
    path("school_register", schoolRegView, name="schoolRegView"),
    path("school" , schoolProfile, name="schoolProfile"),

    # database for debtors
    path("database/", database, name="database"),
    path("debtor_about/<str:pk>", debtorView, name="debtorView")
]
