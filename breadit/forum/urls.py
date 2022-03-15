from django.urls import path

from .views import PostView, PostDetailView, MyProfileView, CreatePostView

urlpatterns = [
    path('', PostView.as_view(), name='index'),
    path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('accounts/profile/', MyProfileView.as_view(), name='profile'),
    path('create_post', CreatePostView.as_view(), name='create_post'),
]