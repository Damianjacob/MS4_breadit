from django.urls import path

from .views import SignUpView, MyAccountView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]