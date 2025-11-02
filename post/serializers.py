from rest_framework import  serializers
from .models import  Category, Article

class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = ["name", "slug", "featured"]

class ArticleSerializer(serializers.ModelSerializer):
    model = Article
    fields = ["name", "image", "slug", "featured"]