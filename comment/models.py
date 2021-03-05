from django.conf import settings
from django.db import models


class Comment(models.Model):
    content = models.TextField('Комментарий')
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey('post.Post', models.SET_NULL, 'comments', null=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.content
