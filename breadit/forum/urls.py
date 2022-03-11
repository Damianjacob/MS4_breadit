from django.urls import path
from . import views

from .views import PostView, PostDetailView

urlpatterns = [
    # path('', views.index, name='index'),

    # class based view path:
    path('', PostView.as_view(), name='index'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]