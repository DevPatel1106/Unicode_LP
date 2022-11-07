from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import CustomUser,admin,agent

class CustomUserCreationForm(UserCreationForm):
    # firstname = forms.CharField( max_length = 50)
    # lastname = forms.CharField( max_length = 50)
    # phonenumber = forms.NumberInput()
    # profilepic =forms.FileField()
    # is_staff =forms.BooleanField(required=False)
    # is_superuser =forms.BooleanField(required=False)
    # is_active =forms.BooleanField(required=False)
    class Meta:
        model = CustomUser
        fields = ["username", "email","phonenumber","profilepic","first_name","last_name"]
        # fields = '__all__'
        # fields = ["username", "email","firstname","lastname","phonenumber","profilepic"]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # filed =('email',)
        fields = '__all__'

class LogInForm (forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

'''class AdminSignInForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ["username", "email","phonenumber","profilepic","first_name","last_name"]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user    

class AgentSignInForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ["username", "email","phonenumber","profilepic","first_name","last_name"]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user'''
