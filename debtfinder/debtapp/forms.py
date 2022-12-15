from .models import *
from django import forms


class ContactForm(forms.Form):
    school_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=50)
    website = forms.EmailField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)



class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ["body", "topics"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
