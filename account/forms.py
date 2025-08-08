from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class EmailLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']