from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.safestring import mark_safe
# from todoapp.models import ToDoList

class CustomUser(AbstractUser):
    username = models.CharField( max_length = 50)
    firstname = models.CharField( max_length = 50,blank=True)
    lastname = models.CharField( max_length = 50,blank=True)
    email = models.EmailField(('email address'), unique = True)
    phonenumber = models.CharField(max_length=10,default=0)
    profilepic = models.ImageField(upload_to='images',default="")

    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False) 
    # is_admin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_agent= models.BooleanField(default=False)

    # normal = 1
    # admin = 2
    # agent =3
      
    # ROLE_CHOICES = (
    #     (normal, 'normal'),
    #     (admin, 'admin'),
    #     (agent, 'agent'),
    # )
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []

    object = CustomUserManager()

    def __str__(self):
        return self.email

    def profile_pic(self):
        return mark_safe('<img src+"{}"width="100" />'.format(self.image.url))
    profile_pic.short_description = 'image'
    profile_pic.allow_tags = True

'''class admin(CustomUser):
    useracc = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True, related_name='adminacc')
    # todolists = models.ManyToManyField(ToDoList, through='ToDoList')
    # is_admin = models.BooleanField(default=True)
    class meta:
        permissions = (
            ("can_add_or_delete_tasks","To Do CRUD")
        )


class agent(CustomUser):
    useracc = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True, related_name='agentacc')
    agentadmin = models.ForeignKey(admin,on_delete=models.CASCADE, related_name='agentadmin',blank=True, null=True)
    # is_agent= models.BooleanField(default=True)
    class meta:
        permissions = (
            ("can_change_completion_status","To change status")
        )'''

 


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