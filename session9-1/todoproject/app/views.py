from django.shortcuts import render, redirect
from .models import TodoList, TodoList_files, TodoList_images, Comment
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

#계정 관리 함수
def signup(request):
    if request.method == 'POST':
        found_user = User.objects.filter(username=request.POST.get('username'))
        if (len(found_user)) > 0:
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', {'error':error})

        new_user = User.objects.create_user(
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('index')
    
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        found_user = auth.authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if found_user is None:
            error = 'Wrong ID or password :('
            return render(request, 'registration/login.html', {'error': error})

        auth.login(request, found_user)    
        return redirect('index')

    return render(request, 'registration/login.html')
    
def logout(request):
    auth.logout(request)

    return redirect('index')
#서버 관리 함수
def index(request):
    todos = TodoList.objects.all().order_by('date_deadline')    
    for todo in todos:
        dif = todo.date_deadline - datetime.date(datetime.now())
        todo.remaining = dif.days
        
    return render(request, 'index.html', {'todos' : todos })

def mytodo(request):
    user = request.user
    mytodos = TodoList.objects.filter(author=user).order_by('date_deadline')    
    for todo in mytodos:
        dif = todo.date_deadline - datetime.date(datetime.now())
        todo.remaining = dif.days
        
    return render(request, 'mytodo.html', {'mytodos' : mytodos })

@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        new_todo = TodoList.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            date_deadline = request.POST['date_deadline'],
            author = request.user
        )
        return redirect('detail', new_todo.pk)

    return render(request, 'new.html')

def detail(request, todo_pk):
    todo = TodoList.objects.get(pk=todo_pk)
    if request.method == 'POST':
        content = request.POST.get('content', '')
        Comment.objects.create(
            todo=todo,
            content=content,
            author = request.user
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