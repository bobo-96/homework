from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField('Пост', max_length=30)
    body = models.TextField('Текст')
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
