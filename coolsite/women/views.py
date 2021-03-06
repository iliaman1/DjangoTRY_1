from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import Women, Comment, AddCommentForm, AddPostForm, ContactForm, RegisterUserForm, LoginUserForm, LoginAjaxForm
from .utils import DataMixin
from abc import ABC


class WomenHome(DataMixin, ListView):
    context_object_name = 'posts'
    queryset = Women.objects.select_related('cat')
    template_name = 'women/index.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(**context, **c_def)


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comment'] = AddCommentForm
        post = context['post']
        c_def = self.get_user_context(title=context['post'], comments=Comment.objects.filter(post=post.pk))
        return dict(**context, **c_def)


class Vote(ABC):
    model = None
    lookup_field = None
    lookup_url_kwargs = None

    @classmethod
    def get_object(cls, **kwargs):
        return get_object_or_404(cls.model, **kwargs)

    @classmethod
    @csrf_exempt
    def like(cls, request, **kwargs):
        obj = cls.get_object(**{cls.lookup_field: kwargs[cls.lookup_url_kwargs]})
        obj.like += 1
        obj.save()
        return HttpResponse(status=200)

    @classmethod
    @csrf_exempt
    def dislike(cls, request, **kwargs):
        obj = cls.get_object(**{cls.lookup_field: kwargs[cls.lookup_url_kwargs]})
        obj.dislike += 1
        obj.save()
        return HttpResponse(status=200)


class PostVote(Vote):
    model = Women
    lookup_field = 'slug'
    lookup_url_kwargs = 'post_slug'


class CommentVote(Vote):
    model = Comment
    lookup_field = 'pk'
    lookup_url_kwargs = 'comment_id'


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


class TopRaited(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 2

    def get_queryset(self):
        return Women.objects.all().order_by(-F('like') + F('dislike')).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Топ дев')
        return dict(**context, **c_def)


class ShowCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 2

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat), cat_selected=self.kwargs['cat_slug'])
        return dict(**context, **c_def)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(**context, **c_def)


class Contact(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Есть контакт')
        return dict(**context, **c_def)

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(**context, **c_def)


class LoginAjax(DataMixin, View):
    def get(self, request):
        context = {
            'login_ajax': LoginAjaxForm()
        }
        return context

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse(data={}, status=201)
            return JsonResponse(
                data={'error': 'Пароль или логин не валидны'},
                status=400
            )
        return JsonResponse(
            data={'error': 'Введите логин и пароль'},
            status=400
        )



class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(**context, **c_def)

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
