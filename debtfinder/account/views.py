from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
# Registration for users

# Creates a custom user and a parent

def createAccount(request):
    return render(request, "account/create_account.html")

def registerView(request):
    form = CustomUserForm()
    parent = ParentForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        parent = ParentForm(request.POST)
        if form.is_valid() and parent.is_valid():
            user = form.save(commit=False)
           
            if user.isParent == True and user.isSchool == True:
               messages.error(request, "You can't choose both")
                
            elif user.isSchool == True:
               messages.error(request, "You can't choose school")
            elif user.isParent == False:
                messages.error(request, "You have to tick As a Parent")
            elif user.isParent == True:
                user.save()
                messages.success(request, "You're now been redirected to verify your account")
                Parent.objects.create(
                    parent=user,
                    student_id = request.POST.get('student_id'),
                    first_name = request.POST.get('first_name'),
                    last_name = request.POST.get('last_name'),
                    email = request.POST.get('email'),
                    phone_number = request.POST.get('phone_number'),
                )
                return redirect("userProfile")

    context = {
        "form": form,
        "parent": parent
    }
    return render(request, "account/register.html", context)
# Registration for schools


# When a school is created, it creates a custom user, too.


def schoolRegView(request):
    school = SchoolForm()
    reg = CustomUserForm()
    if request.method == "POST":
        reg = CustomUserForm(request.POST)
        school = SchoolForm(request.POST)
        if reg.is_valid() and school.is_valid():
            user = reg.save(commit=False)
            if user.isParent == True and user.isSchool == True:
               messages.error(request, "You can't choose both")
                
            elif user.isParent == True:
               messages.error(request, "You can't choose Parent")
            elif user.isSchool == False:
                messages.error(request, "You can't continue without choosing School")
            elif user.isSchool == True:
                user.save()
                School.objects.create(
                    school=user,
                    school_name=request.POST.get('school_name'),
                    CAC_Reg_number=request.POST['CAC_Reg_number'],
                )
                return redirect("schoolProfile")
    else:
        messages.error(request, "An error has occurred. Try again")
    context = {
        "form": reg,
        "school": school
    }
    return render(request, "account/school_register.html", context)

# Log in and Log out for all users


def loginView(request):
    if request.user.is_authenticated:
        return redirect("homepage")
        
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        """
         try:
            user = user.objects.get(email=email)
        except:
            messages.info(request, "Account doesn't exist")
        """
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("homepage")
        messages.info(request, "Account not found. Credentials incorrect")
        redirect("login")
    return render(request, "account/login.html")


def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You're not logged out")
        return redirect("login")
    else:
        messages.info(request, "You're not signed in")
        return redirect("homepage") 

@login_required
def schoolProfile(request):
    return render(request, "account/schoolProfile.html")

@login_required
def schools(request):
    schoolList = School.objects.all()
    context = {
        "schoolList": schoolList
    }
    return render(request, "", context)

@login_required
def school_view(request, pk):
    schoolView = School.objects.get(id=pk)
    context = {
        "schoolView": schoolView
    }
    return render(request, "", context)
@login_required
def database(request):
    debtors = Debtor.objects.all()
    context = {
        "debtors": debtors
    }

    return render(request, "", context)

@login_required
def debtorView(request, pk):
    debtorView = Debtor.objects.get(id=pk)
    context = {
        "debtor": debtorView
    }
    return render(request, "", context)
