from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *


def index(request):
    posts = Women.objects.all()
    context = {'title': 'Главная страница',
               'posts': posts,
               'cat_selected': 0}
    return render(request, 'women/index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    if request.method == 'POST':
        if request.POST.get('like'):
            post.like += 1
            post.save()
        elif request.POST.get('dislike'):
            post.like -= 1
            post.save()
    context = {'post': post, 'title': post.title, 'cat_selected': post.cat_id}
    return render(request, 'women/post.html', context=context)


def add_like(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    post.like += 1
    post.save()
    context = {'post': post, 'title': post.title, 'cat_selected': post.cat_id}
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
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()

    return render(request, 'women/addpage.html', {'title': 'Добавление статьи', 'form': form, })


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')