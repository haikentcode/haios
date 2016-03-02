from django import forms
from django.forms import ModelForm
from models import *


class FeedBack(forms.Form):
    TOPIC_CHOICES=(('general', 'General enquiry'),('bug', 'Bug report'),('suggestion', 'Suggestion'))
    topic=forms.ChoiceField(choices=TOPIC_CHOICES)
    message=forms.CharField(widget=forms.Textarea(),initial="What You Think ?")
    sender=forms.EmailField(required=False)


class Student(ModelForm):
   class Meta:
       model = Student
       fields = ['name','gender','contactNo','image']


""""
ugly way to include class in from feild
x=forms.PasswordInput(attrs={'class':'form-control'})
y=forms.MultipleHiddenInput(attrs={'class':'form-control'})
TOPIC_CHOICES=(('general', 'General enquiry'),('bug', 'Bug report'),('suggestion', 'Suggestion'))
topic=forms.ChoiceField(choices=TOPIC_CHOICES,widget=y)
message=forms.CharField(widget=forms.Textarea(),initial="What You Think ?")
sender=forms.EmailField(required=False,widget=x,max_length=254)
"""
