from django.contrib import admin
from .models import *



# Register your models here.
admin.site.register(CustomUser)
admin.site.register(School)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Debtor)
admin.site.register(Contention)