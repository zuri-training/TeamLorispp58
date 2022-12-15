from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="homepage"),
    path("about_us/", aboutUs, name="aboutUs"),
    path("contact_us/", contactUs, name="contactUs"),
    path("frequently_answered_quest", fAQ, name="fAQ"),
    path("schools", schools, name="schools"),
    path("school/<str:pk>/", school, name="school"),
    path("database", database, name="database"),
    path("add_debtor", addDebtor, name="addDebtor"),
    path("deletedebt", deleteDebtor, name="deletedebt"),

    path("contend", contention, name="contend"),


    path("settings", setting, name="setting")

    
]
