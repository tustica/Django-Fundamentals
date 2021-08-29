from django import forms
from django.db.models.fields import CharField
from django.forms import ModelForm
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    # first_name = forms.CharField(max_length=255)
    # last_name = forms.CharField(max_length=255)
    # email = forms.EmailField()
    # password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    # confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput)

class CreateUserForm(UserCreationForm):
    first_name = User.first_name
    email = EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) == 0:
            raise ValidationError("Enter a first name")
        return first_name
        