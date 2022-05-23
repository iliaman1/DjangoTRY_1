from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения women.")


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>ARhiv PO GODAM</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')