from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.


def index(request):
    todo_list = Todo.objects.order_by('-id')

    form = TodoForm()

    context = {'todo_list': todo_list, 'form': form}

    return render(request, 'todo/index.html', context)


def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        user_added_todo = Todo(input_text=form.cleaned_data['input_text'])
        user_added_todo.save()

    return redirect('index')


def makeCompleteTodo(request, todoId):
    todo = Todo.objects.get(pk=todoId)
    todo.complete_todo = True
    todo.save()

    return redirect('index')


def makeUnCompleteTodo(request, todo_ID):
    todo = Todo.objects.get(pk=todo_ID)
    todo.complete_todo = False
    todo.save()

    return redirect('index')


def deleteCompletedTodo(request):
    Todo.objects.filter(complete_todo__exact=True).delete()

    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')
