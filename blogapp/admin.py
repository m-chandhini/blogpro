from django.contrib import admin

# Register your models here.
from blogapp.models import BlogPost
admin.site.register(BlogPost)