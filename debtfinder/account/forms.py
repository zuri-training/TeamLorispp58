from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone_number","isParent", "isSchool",
         "password1", "password2"]
        widgets = {
            'first_name': forms.TextInput(attrs={'required':True, 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'required':True, 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'required':True, 'placeholder': 'Email Address'}),
            
            'phone_number': forms.TextInput(attrs={'required': True, 'placeholder': 'Phone Number'}),
            'password1': forms.PasswordInput(attrs={'required':True, 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'required':True, 'placeholder': 'Confirm your password'})
        }

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "isParent": "As a Parent?",
            "isSchool": "As a School?"
        }


class ParentForm(ModelForm):

    class Meta:
        model = Parent
        fields = ["student_id"]

        labels = {
            "student_id": "Child's ID",
        }


class SchoolForm(ModelForm):

    class Meta:
        model = School
        fields = ["school_name", "CAC_Reg_number","school_address","school_email",
                  "school_phone_number"]


class DebtorForm(ModelForm):
    
    class Meta:
        model = Debtor
        fields = '__all__'


class ContentionForm(ModelForm):
    
    class Meta:
        model = Contention
        fields = '__all__'

