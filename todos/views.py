from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib.auth.forms import UserCreationForm


def index(request):

    todos = Todo.objects.all()[:10]

    context = {'name': 'Kirk Alain', 'todos': todos}
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


def register(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todos/')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'reg_form.html', args)