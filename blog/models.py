from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    # Поля с unique = True индексируются автоматом
    slug = models.SlugField(max_length=150, unique=True)
    # blank = True означает, что это поле может быть пустым
    body = models.TextField(blank=True, db_index=True)
    # auto_now_add = True означает, что дата и время определятся в момент создания объекта
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)
