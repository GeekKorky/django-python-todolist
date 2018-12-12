from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
from todos.forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def index(request):

    todos = Todo.objects.all()[:10]

    context = {'name': 'Kirk Alain', 'todos': todos}
    return render(request, 'index.html', context)


def details(request, id):

    todo = Todo.objects.get(id=id)

    context = {'todo': todo}
    return render(request, 'details.html', context)


@login_required
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
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:

        todo = Todo.objects.get(id=id)

        context = {'todo': todo}

        return render(request, 'edit.html', context)


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