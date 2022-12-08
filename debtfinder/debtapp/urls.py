from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="homepage"),
    path("about_us/", aboutUs, name="aboutUs"),
    path("contact_us/", contactUs, name="contactUs"),
    # discussion
    path("discussions/", discussions, name="discussions"),
    path("discussion/<str:pk>", discussView, name="discussView"),
    path("create_discussion/", createDiscuss, name="createDiscuss"),
    path("update_discussion/", updateDiscuss, name="updateDiscuss"),
    path("delete_discussion/", deleteDiscuss, name="deleteDiscuss"),
    # database for debtors
    path("database/", database, name="database"),
    path("debtor_about/<str:pk>", debtorView, name="debtorView")
]
