from django.shortcuts import render, redirect
from django.http import HttpResponse
from todos.models import Friend
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from todos.forms import EditProfileForm
from todos.forms import EditUserProfileForm
from django.contrib.auth import update_session_auth_hash
from .models import Accounts


def index(request):
    return redirect('/todos/login/')


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)


def view_profile_with_pk(request, id):

    user = User.objects.get(id=id)

    args = {'user': user}
    return render(request, 'profile.html', args)


def edit_profile(request):
    content = {}
    profile = request.user.accounts
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        form2 = EditUserProfileForm(
            request.POST, request.FILES, instance=profile)
        content['form'] = form
        content['form2'] = form2

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            #handle_uploaded_file(request.FILES['file'])
            return redirect('/accounts/profile')

        else:

            content['form.errors'] = form.errors
            content['form2.errors'] = form2.errors

    else:
        form = EditProfileForm(instance=request.user)
        form2 = EditUserProfileForm(instance=profile)
        content['form'] = form
        content['form2'] = form2

        return render(request, 'edit_profile.html', content)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/profile/password/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)


def change_friends(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, new_friend)
    return redirect('/todos/')
