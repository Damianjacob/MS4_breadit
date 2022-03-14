from django.urls import path
from . import views

from .views import PostView, PostDetailView

urlpatterns = [
    path('', PostView.as_view(), name='index'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]