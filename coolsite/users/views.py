from django.shortcuts import render
from django.views.generic import DetailView
from women.utils import DataMixin
from women.forms import RegisterUserForm


class ShowProfile(DataMixin, DetailView):
    model = RegisterUserForm
    template_name = 'users/profile.html'
    slug_url_kwarg = 'username'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='profile')
        return dict(**context, **c_def)
