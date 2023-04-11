from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.Register(Topic)

admin.site.Register(webpage)

admin.site.Register(AccessREcord)


