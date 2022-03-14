from django.urls import path

from .views import PostView, PostDetailView, MyProfileView

urlpatterns = [
    path('', PostView.as_view(), name='index'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('accounts/profile/', MyProfileView.as_view(), name='profile')
]