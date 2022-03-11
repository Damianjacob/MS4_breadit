from django.urls import path
from . import views

from .views import PostView

urlpatterns = [
    # path('', views.index, name='index'),

    # class based view path:
    path('', PostView.as_view()),
]