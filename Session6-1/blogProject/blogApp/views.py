from django.shortcuts import render, redirect
from .models import Article, Category
# Create your views here.
def index(request):
    articles = Article.objects.all()
    drama_category = Category.objects.get(name="drama")
    movie_category = Category.objects.get(name='movie')
    programming_category = Category.objects.get(name='programming')
    drama_count = Article.objects.filter(category=drama_category).count()
    movie_count = Article.objects.filter(category=movie_category).count()
    programming_count = Article.objects.filter(category=programming_category).count()
    print(drama_count)
    print(movie_count)
    print(programming_count)
    return render(request, 'index.html', {'articles' : articles, 'drama_count' : drama_count,'movie_count' : movie_count,'programming_count' : programming_count})

def drama(request):
    drama_category = Category.objects.get(name="drama")
    dramas = Article.objects.filter(category=drama_category)
    print("카테고리:",drama_category)
    print("드라마들:",dramas)
    return render(request, 'drama.html', {'dramas' : dramas})

def movie(request):
    movie_category = Category.objects.get(name='movie')
    movies = Article.objects.filter(category=movie_category)
    return render(request, 'movie.html', {'movies' : movies})

def programming(request):
    programming_category = Category.objects.get(name='programming')
    programmings = Article.objects.filter(category=programming_category)
    return render(request, 'programming.html', {'programmings' : programmings})

def new(request):
    if request.method == 'POST' :
        print(request.POST)
        category = Category.objects.get(name=request.POST['category'])
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = category,
        )
        return redirect('detail', article_pk=new_article.pk)
    else:
        return render(request, 'new.html')
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article' : article})

# def blogMain(request):
#     return render(request, 'blogMain.html')
    