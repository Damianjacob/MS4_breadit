from django.urls import path

from .views import PostView, PostDetailView, MyProfileView, CreatePost

urlpatterns = [
    path('', PostView.as_view(), name='index'),
    path('<slug:slug>/<int:id>', PostDetailView.as_view(), name='post_detail'),
    path('accounts/profile/', MyProfileView.as_view(), name='profile'),
    path('create_post', CreatePost.as_view(), name='create_post'),
]