from django.shortcuts import render, redirect
from .models import *
from account.models import *
from account.forms import DebtorForm, ContentionForm
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
                send_mail(subject, message, 'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
            return redirect("homepage")
    return render(request, "contact_us.html")


def fAQ(request):
    return render(request, "faq.html")


@login_required()
def schools(request):
    schoolList = School.objects.all()
    context = {
        "schoolList": schoolList
    }
    return render(request, "listOfSchools.html", context)


@login_required()
def school(request, pk):
    schoolView = School.objects.get(id=pk)
    context = {
        "schoolView": schoolView
    }
    return render(request, "schoolProfilepage.html", context)


@login_required()
def discussions(request):
    discuss = Discussion.objects.all()
    context = {
        "discuss": discuss
    }
    return render(request, "", context)


@login_required()
def discussView(request, pk):
    discussObj = Discussion.objects.get(id=pk)
    context = {
        "discuss": discussObj
    }
    return render(request, "", context)

# create a new discuss


@login_required()
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


@login_required()
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


@login_required()
def deleteDiscuss(request, pk):
    discussObj = Discussion.objects.get(id=pk)
    if request.method == "POST":
        discussObj.delete()
        return redirect("disccuss")
    context = {"object": discussObj}
    return render(request, "", context)


@login_required()
def createComment(request):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("discuss")
    context = {
        "form": form
    }
    return render(request, "", context)


@login_required()
def updateComment(request, pk):
    commentObj = Comment.objects.get(pk=id)
    form = CommentForm(instance=commentObj)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=commentObj)
        if form.is_valid():
            form.save()
            return redirect("discuss")
    context = {
        "form": form
    }
    return render(request, "", context)


@login_required()
def deleteComment(request, pk):
    commentObj = Comment.objects.get(id=pk)
    if request.method == "POST":
        commentObj.delete()
        messages.success(request, "Comment deleted successfully")
        return redirect("discuss")
    context = {
        "object": commentObj
    }
    return render(request, "", context)


@login_required()
def database(request):
    debtors = Debtor.objects.all()
    context = {
        "debtors": debtors
    }

    return render(request, "", context)

@login_required()
def debtorView(request, pk):
    debtorView = Debtor.objects.get(id=pk)
    context = {
        "debtor": debtorView
    }
    return render(request, "", context)


@login_required()
def addDebtor(request):
    form = DebtorForm()
    if request.user.isParent == True:
        messages.error(request, "You can't access this page")
    elif request.user.isSchool == True:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "You've succefully added a debtor")
                return render("debtor")
        else:
            messages.error(request, "An error has occurred")
    context = {
        "form": form
    }
    return render(request, "", context)


@login_required()
def deleteDebtor(request):
    if request.user.isParent == True:
        messages.info(
            request, "You cannot access this page. You can only contend. If contention is passed, request the school to delete it")
        return redirect("debtor")
    elif request.user.isSchool == True:
        if form.is_valid():
            form.delete()
            return redirect(debtor)
    context = {
        "form": form
    }
    return render(request, "", context)

@login_required()
def contention(request):
    form = ContentionForm()
    if request.method == "POST":
        form = ContentionForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            if user.request.isParent == True:
                req.save()
                return redirect("debtor")
        else:
            messages.error(request, "Sorry, an error occurred")
    context = {
        "form": form
    }
    return render(request, "", context)

@login_required()
def setting(request):
    return render(request, "settings.html")
