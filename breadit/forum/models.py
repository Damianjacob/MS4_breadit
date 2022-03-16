from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
from django.urls import reverse
import uuid

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=False, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = CloudinaryField('image', blank=True, null=True)
    video = CloudinaryField(resource_type='video', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    uuid = uuid.uuid4()

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    
    def number_of_comments(self):
        return self.comments.count()
    
    class Meta:
        ordering = ['-created_on']

    # The following two methods have been copied and adapted from this article:
    # https://learndjango.com/tutorials/django-slug-tutorial
    # Consider using following method if time allows
    # https://docs.djangoproject.com/en/dev/ref/forms/validation/#validating-fields-with-clean

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={
                'slug': self.slug
            })

    def save(self, *args, **kwargs):
        if not self.slug:
            title_and_uuid = self.slug + ' ' + str(self.uuid)
            self.slug = slugify(title_and_uuid)
        return super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment "{self.content[0:50]}..." by {self.author}'

    class Meta:
        ordering = ['created_on']
