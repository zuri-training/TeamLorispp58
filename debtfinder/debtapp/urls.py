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

    path("schools", schools, name="schools"),
    path("school/<str:pk>/", school, name="school"),
    path("settings", setting, name="setting")

    
]
