from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *


def index(request):
    posts = Women.objects.all()
    context = {'title': 'Главная страница',
               'posts': posts,
               'cat_selected': 0}
    return render(request, 'women/index.html', context=context)


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с ид = {post_id}")


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts)==0:
        raise Http404()

    context = {'title': 'Отображение по рубрикам',
               'posts': posts,
               'cat_selected': cat_id}
    return render(request, 'women/index.html', context=context)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')