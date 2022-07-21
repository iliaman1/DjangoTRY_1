from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='profile URL')
    fio = models.CharField('ФИО', max_length=255, default='')
    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField('Дата рождения', default='2004-09-12')
    ava = models.ImageField(upload_to="avas/%Y/%m/%d/", verbose_name='Аватар')

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_slug': self.slug})