
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone_number","isParent", "isSchool",
         "password1", "password2"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
        }


class ParentForm(ModelForm):

    class Meta:
        model = Parent
        fields = ["student_id", "address",
                  "gender",  "profile_picture", "religion",
                  "local_govt_area", "state"]

        labels = {
            "student_id": "Child's ID",
            "gender": "Your Gender"
        }


class SchoolForm(ModelForm):

    class Meta:
        model = School
        fields = ["school_name","CAC_Reg_number","school_address","school_email",
                  "school_phone_number","school_logo","website",
                  "district_code","local_govt_area","state"]


class DebtorForm(ModelForm):
    
    class Meta:
        model = Debtor
        fields = '__all__'


class ContentionForm(ModelForm):
    
    class Meta:
        model = Contention
        fields = '__all__'

