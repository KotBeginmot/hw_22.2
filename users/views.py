import random

from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserForm, UserUpdateForm
from users.models import User


# Create your views here.
class LIView(LoginView):
    template_name = 'users/login.html'


class LOView(LogoutView):
    template_name = 'users/logout.html'


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('catalog:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        verification = random.randint(100000, 999999)
        new_user = form.save()
        send_mail(
            subject='Верификация',
            message=f'http://127.0.0.1:8000/users/verification/{verification}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        new_user.verification = verification

        return super().form_valid(form)


def verification(request, pk):
    for i in User.objects.all():
        if i.verification == pk and i.email == User.objects.get(verification=pk).email:
            context = {'object': 'SUCCESS'}
            break
        else:
            context = {'object': 'ERROR'}

    return render(request, 'users/verification.html', context)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:update')
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user


def genpass(request):
    password = str(random.randint(0, 999999))
    request.user.set_password(password)
    request.user.save()
    send_mail(
        subject='Генерация пароля',
        message=f'{password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    return redirect(reverse('users:login'))

