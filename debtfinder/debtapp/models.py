from django.conf import settings

from django.db import models


# Create your models here.
class Discussion(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Creator")
    created_on = models.TimeField(auto_now=True)
    updated_on = models.TimeField(auto_now=True)
    body = models.TextField()
    topics = models.ManyToManyField("Topic")

class Comment(models.Model):
    comment_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name="Comment By")
    body = models.TextField()
    created_on = models.TimeField(auto_now=True)
    updated_on = models.TimeField(auto_now=True)

    def __str__(self):
        return self.body

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    