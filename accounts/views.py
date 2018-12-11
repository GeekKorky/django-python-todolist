from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Accounts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


def index(request):
    return HttpResponse('Home Accounts')


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)