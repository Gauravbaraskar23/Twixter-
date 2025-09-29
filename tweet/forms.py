from django import forms 
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm) :
    class Meta:
        model = Tweet
        fields = ['text' , 'photo'] 
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        #built in functios pr tuple use krte hai.
        fields = ('username' , 'email' , 'password1' , 'password2')   
