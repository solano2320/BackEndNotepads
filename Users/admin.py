from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'birth_date', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birth_date',)}), 
    )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('birth_date')}),)

admin.site.register(CustomUser, CustomUserAdmin)