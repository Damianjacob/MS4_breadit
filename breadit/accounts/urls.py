from django.urls import path

from .views import SignUpView, MyProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('/<str:username>', MyProfileView.as_view(), name='profile'),
]