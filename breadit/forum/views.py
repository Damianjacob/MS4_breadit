from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Post, Comment

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
            'comments': comments
        })

    template_name = 'post_detail.html'