from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserAppDetails)
admin.site.register(Plan)
admin.site.register(Database)
admin.site.register(EnvironmentVariable) 
