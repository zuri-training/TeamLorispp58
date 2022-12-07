from django.db import models
import uuid


# model for school
class School(models.Models):
    school_name = models.CharField(max_length=250)
    school_address = models.CharField(max_length=250)
    CAC_reg_number = models.IntegerField(max_length=10)
    school_email = models.EmailField(max_length=254)
    school_phone_number = models.IntegerField()
    website = models.CharField(max_length=100, blank=True, null=True)
    local_govt_area = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    owner_first_name = models.CharField(max_length=200)
    owner_last_name = models.CharField(max_length=200)
    owner_phone_number = models.IntegerField()
    owner_email = models.EmailField(max_length=254)
    owner_address = models.CharField(max_length=250)

    def __str__(self):
        return self.school_name
    
class Student(models.Model):
    reg_code = models.CharField(max_length=10)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    religion = models.CharField(max_length=50)
    isDisabled = models.BooleanField(blank=True, null=True)
    disability = models.CharField(max_length=200, blank=True, null=True)
    hobbies = models.CharField(max_length=200, blank=True, null=True)
    sports = models.CharField(max_length=200, blank=True, null=True)
    school_enrolled = models.ForeignKey(School, on_delete=models.CASCADE)
    previous_school = models.CharField(max_length=250)
    parent_full_name = models.CharField(max_length=500)
    parent_phone_number = models.IntegerField(max_length=11)
    parent_email = models.EmailField(max_length=254)
    parent_occupation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.reg_code} : {self.first_name}, {self.last_name}"
    