from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def todo(request, sort = 'addDate', order = 'asc'):
    sort_by = request.POST.get('sort', 'addDate')
    order_by = request.POST.get('order', 'asc')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')

    form = TodoForm()

    if sort_by == 'addDate':
        if order_by == 'asc':
            todos = Todo.objects.all().order_by(f'id')
        else:
            todos = Todo.objects.all().order_by(f'-id')
    else:
        if order_by == 'asc':
            todos = Todo.objects.all().order_by(f'{sort_by}')
        else:
            todos = Todo.objects.all().order_by(f'-{sort_by}')

    data = {
        'form': form,
        'todos': todos,
        'sort_by': sort_by,
        'order_by': order_by
    }
    return render(request, 'todo/todo.html', data)

def editTodo(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo.title = form.cleaned_data['title']
            todo.dueDate = form.cleaned_data['dueDate']
            todo.addDate = form.cleaned_data['addDate']
            todo.status = form.cleaned_data['status']
            todo.save()
            return redirect('todo')
    else:
        form = TodoForm(instance=todo)

    data = {
        'todo': todo,
        'form': form,
    }
    return render(request, 'todo/todo-update.html', data)


def deleteTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/todo')

def update_todo_status(request, pk):
    todo = Todo.objects.get(id=pk)
    print(str(pk) + " " + str(todo.status))
    todo.status = not todo.status
    todo.save()
    return redirect('/todo')