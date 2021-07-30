from django import forms

from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username','email','institution', 'city', 'country', 'password']
