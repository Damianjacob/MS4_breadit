from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm, CommentForm
from django.urls import reverse


# Create your views here.


# Class-based view for the index page (which contains the posts)
class PostView(ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    post_list = queryset
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(request, 'post_detail.html', {
            'post': post,
            'slug': slug,
            'comments': comments,
            'comment_form': CommentForm(),
            'liked':liked,
        })

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('created_on')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(self.request, 'Your comment has been created succesfully!')
        else:
            comment_form = CommentForm()

        return render(request, 'post_detail.html', {
            'post': post,
            'slug': slug,
            'comments': comments,
            'comment_form': CommentForm()
        })

class PostLike(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Class-based view for the creation of posts, limited to logged-in users
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    template_name = 'create_post_form.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        files = self.request.FILES

        # The following if statement checks if any new image was submitted,
        # and only tries to save that image  if that's the case.
        if 'post_file' in files:
            form.instance.image = files['post_file']

        form.save()
        messages.success(self.request, 'Your post has been created succesfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    form_class = PostForm
    model = Post
    template_name = 'update_post_form'

    def get(self, request, slug):
        """
        method for get requests. In this case it is used
        only to check if the user and the author of the post 
        are the same, and raises a 403 error otherwise. This is to avoid 
        malicious url manipulation.
        """
        post = get_object_or_404(Post, slug=slug)
        user = request.user
        if str(user.username) != str(post.author):
            raise PermissionDenied
        else:
            return render(request, 'update_post_form.html', {
                'post': post,
                'slug': slug
            })

    def form_valid(self, form):
        files = self.request.FILES
        # The following if statement checks if any new image was submitted,
        # and only tries to save a new image if that's the case.
        if 'post_file' in files:
            form.instance.image = files['post_file']
        form.save()
        messages.success(self.request, 'Your post has been updated succesfully!')
        return super().form_valid(form)

class DeletePostView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = '/'
    success_message = "Your post has been deleted succesfully!"
    
    def get(self, request, slug):
        """
        method for get requests. In this case it is used
        only to check if the user and the author of the post 
        are the same, and raises a 403 error otherwise. This is to avoid 
        malicious url manipulation.
        """
        post = get_object_or_404(Post, slug=slug)
        user = request.user
        if str(user.username) != str(post.author):
            raise PermissionDenied
        else:
            return render(request, 'post_confirm_delete.html', {
                'post': post,
                'slug': slug
            })
    
    def delete(self, request, slug):
        messages.success(self.request, self.success_message)
        return super(DeletePostView, self).delete(request, slug)


