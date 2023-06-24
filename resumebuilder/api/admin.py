from django.contrib import admin
from api.models import profile


# Register your models here.
@admin.register(profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'dob', 'state', 'gender', 'location', 'pimage', 'rdoc']


