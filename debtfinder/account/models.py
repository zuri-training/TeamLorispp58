from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .user import CustomUserManager
import uuid

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

"""
Go through the customUser model.
"""

class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=11)
    isParent = models.BooleanField(default=False)
    isSchool = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    object = CustomUserManager()

    class Meta:
        ordering = ["-email"]
        verbose_name = 'User'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class School(models.Model):
    school = models.OneToOneField(settings.AUTH_USER_MODEL, limit_choices_to={
                                  'isSchool': True}, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=250)
    CAC_Reg_number = models.CharField(max_length=10)
    school_address = models.CharField(max_length=250)
    school_email = models.EmailField(max_length=100)
    school_phone_number = models.CharField(max_length=11)
    school_logo = models.FileField(
        upload_to="img", default="", blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    district_code = models.CharField(max_length=5)
    local_govt_area = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    unique_number = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return f"{self.school_name}"


class Parent(models.Model):
    parent = models.OneToOneField(settings.AUTH_USER_MODEL, limit_choices_to={
                                  'isParent': True}, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=11)
    student_id = models.CharField(max_length=16)
    profile_picture = models.FileField(
        upload_to="img", default="", blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    religion = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    local_govt_area = models.CharField(max_length=100)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.parent}"


class Student(models.Model):
    student_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    parent = models.OneToOneField(settings.AUTH_USER_MODEL, limit_choices_to={
                                  'isParent': True}, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id[:6], self.first_name


class Debtor(models.Model):
    posted_by = models.ForeignKey(School, on_delete=models.CASCADE)
    parent_details = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={
                                       'isParent': True}, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    debt_type = models.CharField(max_length=150)
    amount_owed = models.FloatField()
    academic_session = models.DateField()

    def str(self):
        return f"{self.first_name}"


class Contention(models.Model):
    parent_contending = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={
                                          'isParent': True}, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    reason = models.TextField()
    proof = models.FileField(upload_to="img")

    def __str__(self):
        return self.reason[:60]
