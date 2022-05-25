from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'title': 'Главная страница', 'menu': menu, 'posts': posts})


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>ARhiv PO GODAM</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')