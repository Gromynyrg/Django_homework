from django.db import models
from django.urls import reverse
from .libs.slugify import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name="Название категории")

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1, verbose_name="Категория")
    slug = models.SlugField('url', max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

