from django.urls import path

from .views import SignUpView, MyAccountView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<str:username>', MyAccountView.as_view(), name='user_account'),
    # path('/profile/', ProfileView.as_view(), name='profile'),
]