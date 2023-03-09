from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
import django.contrib.auth.models
from .models import User,Employees,Country,City,Way,Hotel,Place,Tour,Comment

# User=get_user_model()
# @admin.register(User)
# class UserAdmin(UserAdmin):
#     pass
admin.site.register(User)
admin.site.register(Employees)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Way)
admin.site.register(Hotel)
admin.site.register(Place)
admin.site.register(Tour)
admin.site.register(Comment)