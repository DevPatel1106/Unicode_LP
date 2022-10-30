from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.safestring import mark_safe

class CustomUser(AbstractUser):
    username = models.CharField( max_length = 50)
    firstname = models.CharField( max_length = 50,blank=True)
    lastname = models.CharField( max_length = 50,blank=True)
    email = models.EmailField(('email address'), unique = True)
    phonenumber = models.CharField(max_length=10,default=0)
    profilepic = models.ImageField(upload_to='images',default="")

    # is_active = models.BooleanField(default=True)
    # staff = models.BooleanField(default=False) 
    # admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []

    object = CustomUserManager()

    def __str__(self):
        return self.email

    def profile_pic(self):
        return mark_safe('<img src+"{}"width="100" />'.format(self.image.url))
    profile_pic.short_description = 'image'
    profile_pic.allow_tags = True

# Email address: dev@gmail.com
# Phonenumber: 9372846613
# Profilepic:  
# Password: password
# Password (again):
# This password is too common.
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.

# Email address: admin@gmail.com
# Phonenumber: 9372846613
# Profilepic:  
# Password: password
# Password (again):
# This password is too common.
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.

# Email address: adminuser@gmail.com
# Phonenumber: 9372846613
# Profilepic:  
# Password: pass
# Password (again): 
# This password is too short. It must contain at least 8 characters.
# This password is too common.
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.