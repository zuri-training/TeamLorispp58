from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import DiscussionForm, CommentForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, "index.html")


def aboutUs(request):
    return render(request, "about_us.html")


def contactUs(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = {
                'school_name': form.cleaned_data['school_name'],
                'email': form.cleaned_data['email'],
                'website': form.cleaned_data['website'],
                'message': form.cleaned_data['message']
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
            return redirect ("main:homepage")
    return render(request, "contact_us.html")

def fAQ(request):
    return render(request, "faq.html")

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