from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm
from django.urls import reverse
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

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('created_on')
        return render(request, 'post_detail.html', {
            'post': post,
            'slug': slug,
            'comments': comments,
        })

    template_name = 'post_detail.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    template_name = 'create_post_form.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.image = self.request.post_file
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Post



class MyProfileView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'profile'
    template_name = 'profile.html'