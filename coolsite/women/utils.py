from django.core.paginator import Paginator

from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

    def pagination(self, numbers_pages, request, data):
        paginator = Paginator(data, numbers_pages)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return page_obj
