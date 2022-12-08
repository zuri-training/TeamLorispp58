from django.shortcuts import render
from .models import *

# Create your views here.

def login(request):
    context = {}
    return render(request, "login.html", context)


def logout(request):
    context = {}
    return render(request, "", context)


def school_register(request):
    context = {}
    return render(request, "", context)


def student_register(request):
    context = {}
    return render(request, "", context)


def schools(request):
    schoolList = School.objects.all()
    context = {
        "schoolList": schoolList
    }
    return render(request, "", context)


def school_view(request, pk):
    schoolView = School.objects.get(id=pk)
    context = {
        "schoolView": schoolView
    }
    return render(request, "", context)

"""
def debtors(request):
    debtorList = Debtor.objects.all()
    context = {
        "debtors": debtorList
    }
    return render(request, "", context)


def debtor_view(request, pk):
    debtorView = Debtor.objects.get(id=pk)
    context = {
        "debtor": debtorView
    }
    return render(request, "", context)
"""