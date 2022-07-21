from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, FormView
from women.utils import DataMixin
from women.forms import RegisterUserForm
from users.models import CustomUser


class ShowProfile(DataMixin, DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    slug_url_kwarg = 'user_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='profile')
        return dict(**context, **c_def)




