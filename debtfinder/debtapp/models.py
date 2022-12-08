from django.db import models
from account.models import *

# Create your models here.
class Discussion(models.Model):
    created_by = models.ForeignKey(School, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    topics = models.ManyToManyField("Topic")

class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    