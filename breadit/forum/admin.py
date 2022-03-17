from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post, Comment

# Register your models here.
# add good layout to admin

admin.site.register(Post)
admin.site.register(Comment)