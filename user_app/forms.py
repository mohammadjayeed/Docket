from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class CustomRegistrationForm(UserCreationForm):

    email = forms.EmailField()

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("this email is already registered")

        
        
        return self.cleaned_data['email']
    

    class Meta:
        model = User
        fields = ['username','email','password1','password2']