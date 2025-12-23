from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="")
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=255)
    introduccion = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="")
    content = models.TextField()
    ESTADOS = [
        ("PRODUCCION", "Producción"),
        ("DESARROLLO", "Desarrollo")
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS, default="DESARROLLO") 
    github = models.URLField(blank=True, null=True)
    demo = models.URLField(blank=True, null=True)
    category = models.ManyToManyField(Category, related_name = "article")
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.name