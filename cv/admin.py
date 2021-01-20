from django.contrib import admin
from .models import Profile

# Register your models here.

admin.site.site_title = "CV Generator"
admin.site.site_header = "CV Generator"


admin.site.register(Profile)