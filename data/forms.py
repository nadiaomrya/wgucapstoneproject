from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"

# iterable
FIRST_CHOICES =(
    ("1", "Always"),
    ("2", "Often"),
    ("3", "Sometimes"),
    ("4", "Rarely"),
    ("5", "Never"),
)
  
