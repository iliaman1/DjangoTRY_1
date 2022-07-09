from django.core.paginator import Paginator
from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Топ дев", 'url_name': 'toprait'},
        {'title': "Учим JavaScript", 'url_name': 'learnjs'}]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        context['login_form'] = LoginUserForm
        return context

    def pagination(self, numbers_obj, request, data):
        paginator = Paginator(data, numbers_obj)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return page_obj
