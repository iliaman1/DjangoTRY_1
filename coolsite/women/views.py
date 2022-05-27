from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *


def index(request):
    posts = Women.objects.all()
    context = {'title': 'Главная страница',
               'posts': posts,
               'cat_selected': 0}
    return render(request, 'women/index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {'post': post, 'title': post.title, 'cat_selected': post.cat_id,}
    return render(request, 'women/post.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def show_category(request, cat_slug):
    cats =Category.objects.all()
    cat = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(cat_id=cat.id)

    if len(posts)==0:
        raise Http404()

    context = {'title': cat.name,
               'posts': posts,
               'cats': cats,
               'cat_selected': cat.id}
    return render(request, 'women/index.html', context=context)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')