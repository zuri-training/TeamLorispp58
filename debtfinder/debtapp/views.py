from django.shortcuts import render, redirect
from .models import *
from .forms import DiscussionForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, "index.html")


def aboutUs(request):
    return render(request, "")


def contactUs(request):
    return render(request, "")

@login_required
def discussions(request):
    discuss = Discussion.objects.all()
    context = {
        "discuss": discuss
    }
    return render(request, "", context)

@login_required
def discussView(request, pk):
    discussObj = Discussion.objects.get(id=pk)
    context = {
        "discuss": discussObj
    }
    return render(request, "", context)

# create a new discuss

@login_required
def createDiscuss(request):
    form = DiscussionForm()

    if request.method == "POST":
        form = DiscussionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("discuss")
    context = {"form": form}
    return render(request, "", context)

# update a discuss

@login_required
def updateDiscuss(request, pk):
    discussObj = Discussion.objects.get(id=pk)
    form = DiscussionForm(instance=discussObj)

    if request.method == "POST":
        form = DiscussionForm(request.POST, instance=discussObj)
        if form.is_valid():
            form.save()
            return redirect("discuss")
    context = {"form": form}
    return render(request, "", context)

@login_required
def deleteDiscuss(request, pk):
    discussObj = Discussion.objects.get(id=pk)
    if request.method == "POST":
        discussObj.delete()
        return redirect("disccuss")
    context = {"object": discussObj}
    return render(request, "", context)