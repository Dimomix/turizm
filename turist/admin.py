from django.contrib import admin

# Register your models here.
from .models import User,Employees,Country,City,Way,Hotel,Place,Tour,Comment
admin.site.register(User)
admin.site.register(Employees)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Way)
admin.site.register(Hotel)
admin.site.register(Place)
admin.site.register(Tour)
admin.site.register(Comment)