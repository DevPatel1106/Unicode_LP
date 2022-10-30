from django.contrib import admin

# Register your models here.

from .models import ToDoList,ToDoItem
from django.utils.html import format_html

class ToDoListItemAdmin(admin.ModelAdmin):
    list_display = ('ToDoList', 'title', 'date_of_creation','CompletionStatus','description','daysgiven')
  
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ( 'title','added_by_user','Main_Img')
  
    def active(self, obj):
        return obj.is_active == 1

    def Main_Img(self,obj):
        return format_html('<img src+"{0}" width="auto" height="150px">'.format(obj.image.url))
  
    active.boolean = True


admin.site.register(ToDoList,ToDoListAdmin)
admin.site.register(ToDoItem,ToDoListItemAdmin)

# Username: admin
# Email address: admin@gmail.com
# Password: password