from django.shortcuts import render, redirect
from .models import TodoList, TodoList_files, TodoList_images, Comment
from datetime import datetime
# Create your views here.

def index(request):
    todos = TodoList.objects.all().order_by('date_deadline')    
    for todo in todos:
        dif = todo.date_deadline - datetime.date(datetime.now())
        todo.remaining = dif.days
    return render(request, 'index.html', {'todos' : todos })

def new(request):
    if request.method == 'POST':
        new_todo = TodoList.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            date_deadline = request.POST['date_deadline']
        )
        return redirect('detail', new_todo.pk)

    return render(request, 'new.html')

def detail(request, todo_pk):
    todo = TodoList.objects.get(pk=todo_pk)
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            todo=todo,
            content=content
        )
        return redirect('detail', todo_pk)

    return render(request, 'detail.html', {'todo' : todo})

def edit(request, todo_pk):
    todo = TodoList.objects.get(pk=todo_pk)

    if request.method == 'POST':
        TodoList.objects.filter(pk=todo_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            date_deadline = request.POST['date_deadline']
        )    
        return redirect('detail', todo_pk)
    return render(request, 'edit.html', {'todo' : todo})

def delete(request, todo_pk):
    todo = TodoList.objects.get(pk=todo_pk)
    todo.delete()    
    return redirect('index')

def delete_comment(request, todo_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', todo_pk)