from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import UserBuild, User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.


class RegisterUser(CreateView):
    models = User
    form_class = UserBuild
    success_url = reverse_lazy('tasks:list')
    template_name = 'account/auth.html'

    def post(self, request, *args, **kwargs):
        result = super(RegisterUser, self).post(request, *args, **kwargs)
        user = User.objects.all().last()
        login(request, user)
        return result


def login_user(request):
    if request.method == 'GET':
        form = UserBuild()
        return render(request, 'account/auth.html', {'form': form, 'errors': ''})
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            username = request.POST.get('username', None)
            password = request.POST.get('password1', None)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tasks:list')
            else:
                form = UserBuild(initial={'username': username, 'password1': password})
                return render(request, 'account/auth.html', {'form': form, 'error': 'Invalid Credentials'})
        else:
            return redirect('tasks:list')
