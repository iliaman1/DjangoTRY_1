from django import template
from women.models import *
from django.contrib import auth

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(slug=filter)


@register.inclusion_tag('usertags/list_categories.html')
def show_categories(sort=None, cat_selected=None):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('usertags/list_menu.html')
def show_menu():
    menu = [{'title': "О сайте", 'url_name': 'about'},
            {'title': "Добавить статью", 'url_name': 'add_page'},
            {'title': "Обратная связь", 'url_name': 'contact'},
            {'title': "SQL запросики", 'url_name': 'showsql'},
            {'title': "Топ дев", 'url_name': 'toprait'}]
    # if user.is_authenticated:
    #     menu.pop(1)

    return {"menu": menu}