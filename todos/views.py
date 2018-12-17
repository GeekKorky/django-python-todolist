from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from todos.models import Todo, Friend
from django.contrib.auth.models import User
from todos.forms import RegistrationForm


def index(request):

    todos = Todo.objects.all()[:10]
    users = User.objects.exclude(id=request.user.id)
    try:
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        context = {
            'name': 'Kirk Alain',
            'todos': todos,
            'users': users,
            'friends': friends
        }
        return render(request, 'index.html', context)

    except Friend.DoesNotExist:

        context = {'name': 'Kirk Alain', 'todos': todos, 'users': users}
        return render(request, 'index.html', context)


def details(request, id):

    todo = Todo.objects.get(id=id)

    context = {'todo': todo}
    return render(request, 'details.html', context)


def add(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')


def edit(request, id):
    if (request.method == 'POST'):

        todo = Todo.objects.get(id=id)

        todo.title = request.POST.get('title')
        todo.text = request.POST.get('text')
        todo.save()
        return redirect("/todos")

    else:

        todo = Todo.objects.get(id=id)

        context = {'todo': todo}
        return render(request, 'edit.html', context)


def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/todos")


def register(request):
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/todos")
    else:
        form = RegistrationForm(request.POST)

        args = {'form': form}
        return render(request, 'reg_form.html', args)