from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.db import connection
from .models import *
from .forms import *


class WomenHome(View):
    model = Women  # да это лишняя строчка

    def get(self, request):
        posts = Women.objects.all()
        context = {'title': 'Главная страница',
                   'posts': posts,
                   'cat_selected': 0}
        return render(request, 'women/index.html', context=context)

    # class WomenHome(ListView):
    #     model = Women
    #     template_name = 'women/index.html' #шаблон
    #     context_object_name = 'posts' # меняем название с дефолтного object_list
    #
    #     def get_context_data(self, *, object_list=None, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         context['title'] = 'Главная страница'
    #         context['cat_selected'] = 0
    #         return context
    #
    #     def get_queryset(self):    # Что выбирать из модели Women
    #         return Women.objects.filter(is_published=True)

    # extra_context = {'title': 'Главная страница'} # принимает только неизменияемые(статические данные)
    ''' Если бы меню не передавал в пользовательском теге, передавал бы изменяемый(динамический) контент следующим образом:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu # по этому ключу передавал бы меню (список словарей)
        return context
    '''


class ShowSQL(View):
    form_class = MakeRequest
    template_name = 'women/sql.html'
    success_url = reverse_lazy('showsql')

    def get(self, request):
        form = self.form_class
        context = {'title': 'Запросики',
                   'form': form}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form_class(request.POST)

        context = {
            'title': 'Запросики',
            'form': form,
            'sql': connection.queries
        }
        return render(request, self.template_name, context=context)


# def index(request):
#     posts = Women.objects.all()
#     context = {'title': 'Главная страница',
#                'posts': posts,
#                'cat_selected': 0}
#     return render(request, 'women/index.html', context=context)


# class ShowPost(DetailView):
#     model = Women
#     template_name = 'women/post.html'
#     slug_url_kwarg = 'post_slug' #вместо дефолтного slug
#     #а если по id "pk_url_kwarg"
#     context_object_name = 'post'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['post']
#         return context

# def get_object(self, queryset=None):
#     self.post = get_object_or_404(Women, slug=self.kwargs['post_slug'])
#     return Women.objects.filter(slug=self.kwargs['post_slug'])
#
# def get(self, request, *args, **kwargs):
#     if request.GET.get('like'):
#         self.post.like += 1
#         self.post.save()
#     elif request.GET.get('dislike'):
#         self.post.like -= 1
#         self.post.save()
#     return render(request, 'women/post.html', context=self.get_context_data())

# post = get_object_or_404(Women, slug='post_slug')
# if request.GET.get('like'):
#     post.like += 1
#     post.save()
# elif request.GET.get('dislike'):
#     post.like -= 1
#     post.save()


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     if request.method == 'POST':
#         if request.POST.get('like'):
#             post.like += 1
#             post.save()
#         elif request.POST.get('dislike'):
#             post.like -= 1
#             post.save()
#     context = {'post': post, 'title': post.title, 'cat_selected': post.cat_id}
#     return render(request, 'women/post.html', context=context)


class ShowPost(View):
    form_comment = AddCommentForm
    template_name = 'women/post.html'

    def get(self, request, post_slug):
        post = get_object_or_404(Women, slug=post_slug)
        comments = Comment.objects.filter(post=post.pk)
        form_comment = self.form_comment
        context = {'post': post, 'title': post.title, 'cat_selected': post.cat.slug,
                   'comments': comments, 'form_comment': form_comment}
        return render(request, self.template_name, context=context)

    def post(self, request, post_slug):
        post = get_object_or_404(Women, slug=post_slug)
        comments = Comment.objects.filter(post=post.pk)
        form_comment = self.form_comment(request.POST)
        context = {'post': post, 'title': post.title, 'cat_selected': post.cat.slug,
                   'comments': comments, 'form_comment': form_comment}
        if request.POST.get('like'):
            post.like += 1
            post.save()
        elif request.POST.get('dislike'):
            post.like -= 1
            post.save()
        elif request.POST.get('comment'):
            if form_comment.is_valid():
                email = form_comment.cleaned_data['email']
                content = form_comment.cleaned_data['content']
                go_in_bd = Comment(email=email, content=content, like=0, post=post.pk)
                go_in_bd.save()
            else:
                form_comment = self.form_comment()

        return render(request, self.template_name, context=context)

    # def processing_like(self, request, post):
    #     if request.GET.get('like'):
    #         post.like += 1
    #         post.save()
    #     elif request.GET.get('dislike'):
    #         post.like -= 1
    #         post.save()


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


class ShowCategory(View):
    def get(self, request, cat_slug):
        posts = Women.objects.filter(cat__slug=self.kwargs['cat_slug'])
        # print(posts[0].cat)
        if len(posts) == 0:
            raise Http404

        context = {
            'title': posts[0].cat,  # есть идеи?
            'posts': posts,
            'cat_selected': self.kwargs['cat_slug']
        }
        return render(request, 'women/index.html', context=context)


# class ShowCategory(ListView):
#     model = Category
#     template_name = 'women/index.html'
#     context_object_name = 'posts'
#     allow_empty = False #если пустой список object list вернет 404
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Категория - ' + str(context['posts'][0].cat)
#         context['cat_selected'] = self.kwargs['cat_slug']
#         return context
#
#     def get_queryset(self):
#         return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


# def show_category(request, cat_slug):
#     cats = Category.objects.all()
#     cat = get_object_or_404(Category, slug=cat_slug)
#     posts = Women.objects.filter(cat_id=cat.id)
#
#     if len(posts)==0:
#         raise Http404()
#
#     context = {'title': cat.name,
#                'posts': posts,
#                'cats': cats,
#                'cat_selected': cat.id}
#     return render(request, 'women/index.html', context=context)


class AddPage(View):
    form_class = AddPostForm

    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        form = self.form_class

        context = {'title': 'Добавить статью', 'form': form}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)  # зачем в скобках реквест пост?
        context = {'title': 'Добавить статью', 'form': form}
        if form.is_valid():
            form.save()
        else:
            form = self.form_class()
        return render(request, self.template_name, context=context)


# class AddPage(CreateView):
#     form_class = AddPostForm
#     template_name = 'women/addpage.html'
#     success_url = reverse_lazy('home') #куда идти если не по absolute_url
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Добавить статью'
#         return context


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = AddPostForm()
#
#     return render(request, 'women/addpage.html', {'title': 'Добавление статьи', 'form': form, })


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
