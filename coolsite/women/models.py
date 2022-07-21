from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    like = models.IntegerField(default=0, verbose_name='Лайки')
    dislike = models.IntegerField(default=0, verbose_name='Дизлайки')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['time_create', 'title']


class Comment(models.Model):
    email = models.CharField(max_length=50, verbose_name='Email')
    content = models.TextField(blank=True, verbose_name='Текст коментария')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    like = models.IntegerField(default=0, verbose_name='Лайки')
    dislike = models.IntegerField(default=0, verbose_name='Дизлайки')
    post = models.ForeignKey('Women', on_delete=models.PROTECT, verbose_name='Пост')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.post.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
