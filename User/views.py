from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.views.generic import UpdateView
from .models import MyUser
from django.shortcuts import redirect


class UserRegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UpdateUserView(UpdateView):
    model = MyUser
    form_class = CustomUserChangeForm
    template_name = 'user/updateUser.html'


def loginRedirect(request):
    return redirect('login')
