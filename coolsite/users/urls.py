from django.urls import path, include
from .views import *

urlpatterns = [
    path('profile/<slug:username>', ShowProfile.as_view(), name='profile')
]