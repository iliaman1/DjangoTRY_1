# Generated by Django 4.0.4 on 2022-06-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0004_comment_dislike'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='dislike',
            field=models.IntegerField(default=0, verbose_name='Дизлайки'),
        ),
    ]
