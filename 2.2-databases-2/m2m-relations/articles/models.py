from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(verbose_name='Название тега')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes', verbose_name='РАЗДЕЛ')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='СТАТЬЯ')
    is_main = models.BooleanField(verbose_name='ОСНОВНОЙ')

    class Meta:
        ordering = ['-is_main', 'tag']


