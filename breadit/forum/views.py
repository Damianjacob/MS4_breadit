from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Post, Comment
from django.contrib.auth.models import User

# Create your views here.

# def index(request):
#     post_list = Post.objects.order_by('-created_on')
#     context = {'post_list': post_list}
#     return render(request, 'index.html', context)

# Class-based view for the index page (which contains the posts)
class PostView(ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    post_list = queryset
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post

    def get(self, request, slug, id):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('created_on')
        return render(request, 'post_detail.html', {
            'post': post,
            'slug': slug,
            'comments': comments,
            'id': id
        })

    template_name = 'post_detail.html'


class CreatePost(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'create_post.html'

class MyProfileView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'profile'
    template_name = 'profile.html'