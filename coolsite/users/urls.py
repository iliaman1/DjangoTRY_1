from django.urls import path, include
from .views import *

urlpatterns = [
    path('profile/<slug:user_slug>', ShowProfile.as_view(), name='profile')
]