from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles' : articles})

def detail(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    return render(request, 'detail.html', {'article' : article})

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category']
        )
        return redirect('detail', article_pk = new_article.pk)
    return render(request, 'new.html')

def drama(request):
    dramas = Article.objects.filter(category="drama")
    return render(request, 'drama.html', {'dramas' : dramas})
    
def movie(request):
    movies = Article.objects.filter(category="movies")
    return render(request, 'movie.html', {'movies' : movies})

def programming(request):
    programmings = Article.objects.filter(category="programming")
    return render(request, 'programming.html', {'programmings' : programmings})