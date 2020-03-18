from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post, Categories
# Create your views here.

def detail_post(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'post':post })

def home(request):
    post = Post.objects.filter(state=True)

    return render(request, 'index.html', {'posts': post })

def generals(request):
    posts = Post.objects.filter(
        state = True,
        category=Categories.objects.get(name__iexact='General')
    )
    return render(request, 'generals.html', {'posts': posts})

def games(request):
    posts = Post.objects.filter(
        state=True,
        category=Categories.objects.get(name='Videojuegos')
    )
    return render(request, 'games.html', {'posts': posts})

def programming(request):
    posts = Post.objects.filter(
        state=True,
        category=Categories.objects.get(name='Programación')
    )
    return render(request, 'programming.html',{'posts': posts})

def technology(request):
    posts = Post.objects.filter(
        state=True,
        category=Categories.objects.get(name='Tecnología')
    )
    return render(request, 'technology.html', {'posts': posts})

def tutorials(request):
    posts = Post.objects.filter(
        state=True,
        category=Categories.objects.get(name='Tutoriales')
    )
    return render(request, 'tutorials.html', {'posts': posts})