from .models import *
from django import forms


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
