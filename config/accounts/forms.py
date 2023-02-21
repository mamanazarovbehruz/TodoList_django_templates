from django import forms
from django.forms import ValidationError
from .models import User, Profile

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'tel')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise ValidationError('Parollar bir xil emas!')
        return cd['password2']

class PassUpdateForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)