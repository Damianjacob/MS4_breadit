from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=CASCADE, related_name='posts')
    image = CloudinaryField('image')
    video = CloudinaryField('video')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes')

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    
    class Meta:
        ordering = ['-created_on']