from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")
    slug = models.SlugField(unique=True, max_length=255)
    featured = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Main:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    introduccion = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField(upload_to="")
    body = models.TextField()
    github = models.URLField(max_length=255)
    demo = models.URLField(max_length=255, blank=True, null=True)
    categoria = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def get_absolute_url(self):
        return  reversed('post')

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

