from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post, Categories
from django.db.models import Q
# Create your views here.

def detail_post(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {'post':post })

def home(request):
    queryset = request.GET.get('search')
    post = Post.objects.filter(state=True)
    if queryset:
        post = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset)
        ).distinct()

    return render(request, 'index.html', {'posts': post })

def generals(request):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(
        state = True,
        category=Categories.objects.get(name__iexact='General')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(description__icontains=queryset),
            state=True,
            category=Categories.objects.get(name__iexact='General')
        )

    return render(request, 'generals.html', {'posts': posts})

def games(request):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(
        state=True,
        category=Categories.objects.get(name__iexact='Videojuegos')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(description__icontains=queryset),
            state=True,
            category=Categories.objects.get(name__iexact='Videojuegos')
        )
    return render(request, 'games.html', {'posts': posts})

def programming(request):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(
        state=True,
        category=Categories.objects.get(name__iexact='Programación')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(description__icontains=queryset),
            state=True,
            category=Categories.objects.get(name__iexact='Programación')
        )
    return render(request, 'programming.html',{'posts': posts})

def technology(request):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(
        state=True,
        category=Categories.objects.get(name__iexact='Tecnología')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(description__icontains=queryset),
            state=True,
            category=Categories.objects.get(name__iexact='Tecnología')
        )
    return render(request, 'technology.html', {'posts': posts})

def tutorials(request):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(
        state=True,
        category=Categories.objects.get(name__iexact='Tutoriales')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains=queryset) |
            Q(description__icontains=queryset),
            state=True,
            category=Categories.objects.get(name__iexact='Tutoriales')
        )
    return render(request, 'tutorials.html', {'posts': posts})