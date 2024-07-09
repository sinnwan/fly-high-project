from django.contrib import admin
from .models import LoginUser,user,company

# Register your models here.
admin.site.register(LoginUser)
admin.site.register(company)