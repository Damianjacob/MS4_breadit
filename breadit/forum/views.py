from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post

# Create your views here.

# def index(request):
#     post_list = Post.objects.order_by('-created_on')
#     context = {'post_list': post_list}
#     return render(request, 'index.html', context)

# Creating the class based view for index
class PostView(ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    post_list = queryset
    template_name = 'index.html'
