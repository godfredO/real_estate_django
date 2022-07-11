from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    context={'todo_list':todos}
    return render(request, "todo/todo_list.html", context)


def todo_detail(request, id):
    todo = get_object_or_404(Todo, pk=id)
    context = {'todo':todo}
    return render(request, "todo/todo_detail.html", context)

# CRUD - Create, Retrieve, Update, Delete, List

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, "todo/todo_create.html", context)

def todo_update(request, id):
    todo = get_object_or_404(Todo, pk=id)
    form = TodoForm(request.POST or None, instance= todo)
    if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, "todo/todo_update.html", context)


def todo_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo.delete()
    return redirect('/')
