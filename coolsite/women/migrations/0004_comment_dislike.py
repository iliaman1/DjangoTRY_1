# Generated by Django 4.0.4 on 2022-06-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislike',
            field=models.IntegerField(default=0, verbose_name='Дизлайки'),
        ),
    ]