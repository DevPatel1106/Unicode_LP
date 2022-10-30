from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.models import User
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','is_staff','is_active','phonenumber','profilepic','username','firstname','lastname')
    list_filter = ('email','is_staff','is_active','username')
    fieldsets = (
        (None, {'fields':('email','password','phonenumber','profilepic','username','firstname','lastname')}),
        ('Permissions', {'fields': ('is_staff','is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','phonenumber','profilepic','firstname','lastname','username')}
        ),
    )
    search_fields = ('email','phonenumber','firstname','lastname','username','firstname','lastname')
    ordering = ('email','is_staff', 'is_active','phonenumber','profilepic','username')

admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)