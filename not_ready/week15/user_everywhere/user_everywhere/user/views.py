from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy

from .models import User
from .decorators import login_required, annon_required


def home(request):
    if request.method == 'POST':
        return redirect(reverse('login'))
    return render(request, 'index.html', locals())


@annon_required(redirect_url=reverse_lazy('profile'))
def register(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.exists(email):
            u = User(email=email,
                     password=password)
            u.save()
        else:
            error = "User already exists"
        return redirect(reverse('profile'))

    return render(request, 'register.html', locals())


@annon_required(redirect_url=reverse_lazy('profile'))
def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        u = User.login_user(email, password)

        if u is None:
            error = 'Wrong username or password'
        else:
            request.session['email'] = email
            return redirect(reverse('profile'))

    return render(request, 'login.html', locals())


@login_required(redirect_url=reverse_lazy('login'))
def profile(request):
    if request.method == 'POST':
        request.session.flush()
        return redirect(reverse('login'))

    return render(request, 'profile.html', locals())
