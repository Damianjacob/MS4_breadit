from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
# Create your views here.


class SignUpView(SuccessMessageMixin, generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = "Your account has been created successfully, %(username)s! You can now log in."

class MyProfileView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'registration/profile.html'

    # def get(self, request, username):
    #     user = get_object_or_404(User, username=username)
    #     return render(request, 'registration/profile.html', {
    #         'username': user.username
    #     })

    
    def get(self, request, username):
        user = request.user
        # user = get_object_or_404(User, username=username)
        # The following statement denies access to another user's profile if someone
        # should try to access it through url manipulation
        if user.username != username:
            raise PermissionDenied
        else:
            return render(request, 'registration/profile.html', {
                'username': user.username
            })