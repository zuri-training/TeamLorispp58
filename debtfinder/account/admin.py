from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["school_name"]

admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Debtor)
admin.site.register(Contention)