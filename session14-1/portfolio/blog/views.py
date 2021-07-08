from django.shortcuts import render, redirect
from .models import Post, Comment
# Create your views here.

#웹 페이지 관리
def home(request):
    posts = Post.objects.all().order_by('date_created')
    return render(request, 'home.html')

def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            image = request.POST['image'],
            author = request.user
        )
        return redirect('detail, new_post.pk')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        Comment.objects.create(
            post=post,
            comment=comment,
            author=request.user
        )
        return redirect('detail', post_pk)

    return render(request, 'detail.html', {'post':post})