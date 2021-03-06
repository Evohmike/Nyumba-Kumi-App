from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Neighbourhood,Post,Profile, Business

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name','description','loc','police','health','occupants']

class CreateBizForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude =['user','hood'] 


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =['user','hood'] 

