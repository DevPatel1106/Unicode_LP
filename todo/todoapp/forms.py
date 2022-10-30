from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ToDoList, ToDoItem


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        inbuiltuser = super(UserRegistrationForm, self).save(commit=False)
        inbuiltuser.email = self.cleaned_data['email']
        if commit:
            inbuiltuser.save()
        return inbuiltuser


class createlistform(forms.ModelForm):

    class Meta:
        model = ToDoList
        fields = ["title","Main_Img"]


class listupdateform(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ["ToDoList","title", "description", "CompletionStatus", "daysgiven"]

class deletelistform(forms.ModelForm):

    class Meta:
        model = ToDoList
        fields = ["title",]