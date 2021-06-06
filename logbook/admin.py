from django.contrib import admin
from .models import Workday, Workweek

# Register your models here.

admin.site.register(Workweek)
admin.site.register(Workday)