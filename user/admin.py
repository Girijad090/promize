from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserRegister
# Register your models here.
@admin.register(UserRegister)

class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","phone_no")