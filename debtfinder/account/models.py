from django.db import models
import uuid
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)



# model for school
class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    school_name = models.CharField(primary_key=True, max_length=250)
    school_address = models.CharField(max_length=250)
    cac_reg_number = models.BigIntegerField()
    school_email = models.EmailField(max_length=254)
    school_phone_number = models.BigIntegerField()
    school_logo = models.FileField(upload_to="img", default="")
    website = models.CharField(max_length=100, blank=True, null=True)
    local_govt_area = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    owner_full_name = models.CharField(max_length=250)
    owner_phone_number = models.BigIntegerField()
    owner_email = models.EmailField(max_length=254)
    owner_address = models.CharField(max_length=250)

    def __str__(self):
        return self.school_name


class Parent(models.Model):
    title = models.CharField(max_length=3)
    full_name = models.CharField(primary_key=True, max_length=250)
    phone_number = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_address = models.CharField(max_length=250)
    religion = models.CharField(max_length=50)
    local_govt_area = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100)
    ward = models.ForeignKey("Student", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{ self.title}, {self.full_name}"


class Student(models.Model):
    reg_code = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    religion = models.CharField(max_length=50)
    isDisabled = models.BooleanField(blank=True, null=True)
    disability = models.CharField(max_length=200, blank=True, null=True)
    hobbies = models.CharField(max_length=200, blank=True, null=True)
    sports = models.CharField(max_length=200, blank=True, null=True)
    school_enrolled = models.ForeignKey(School, on_delete=models.PROTECT)
    previous_school = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Debtor(models.Model):
    posted_by = models.ForeignKey(School, on_delete=models.PROTECT)
    student_details = models.ForeignKey(Student, on_delete=models.PROTECT)
    parent_details = models.ForeignKey(Parent, on_delete=models.PROTECT)
    debt_type = models.CharField(max_length=150)
    amount_owed = models.FloatField()
    academic_session = models.DateField()

    def __str__(self):
        return f"{self.posted_by.school_name}"


class Contention(models.Model):
    parent_contending = models.ForeignKey(Parent, on_delete=models.PROTECT)
    student_details = models.ForeignKey(Student, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now=True)
    reason = models.TextField()
    proof = models.FileField(upload_to="img")
    
