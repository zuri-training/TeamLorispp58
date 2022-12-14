from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="homepage"),
    path("about_us/", aboutUs, name="aboutUs"),
    path("contact_us/", contactUs, name="contactUs"),
    path("frequently_answered_quest", fAQ, name="fAQ"),
    # discussion
    path("discussions/", discussions, name="discussions"),
    path("discussion/<str:pk>", discussView, name="discussView"),
    path("create_discussion/", createDiscuss, name="createDiscuss"),
    path("update_discussion/", updateDiscuss, name="updateDiscuss"),
    path("delete_discussion/", deleteDiscuss, name="deleteDiscuss"),

    path("add_comment", createComment, name="addComment"),
    path("edit_comment", updateComment, name="editComment"),
    path("delete_comment", deleteComment, name="addComment"),

    path("schools", schools, name="schools"),
    path("school/<str:pk>/", school, name="school"),
    path("database", database, name="database"),
    path("debtor", debtorView, name="debtor"),
    path("add_debtor", addDebtor, name="addDebtor"),
    path("deletedebt", deleteDebtor, name="deletedebt"),

    path("contend", contention, name="contend"),


    path("settings", setting, name="setting")

    
]
