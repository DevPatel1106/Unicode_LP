

from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.

class ToDoList(models.Model):
    title = models.CharField(max_length=50, primary_key=True, unique=True)
    added_by_user = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    Main_Img = models.ImageField(upload_to='images',default="")
    def __str__(self):
        return self.title
    
    def admin_photo(self):
        return mark_safe('<img src+"{}"width="100" />'.format(self.image.url))
    admin_photo.short_description = 'image'
    admin_photo.allow_tags = True



class ToDoItem(models.Model):
    ToDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE, verbose_name="To Do List")
    title = models.CharField(max_length=50, unique=False)
    description = models.TextField(max_length=500)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    CompletionStatus = models.BooleanField(verbose_name = 'Completion Status')
    daysgiven = models.IntegerField()

    def __str__(self):
        return self.title

