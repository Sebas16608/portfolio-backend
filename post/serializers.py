from rest_framework import  serializers
from .models import  Category, Article

class CategorySerializer(serializers.ModelSerializer):
    class Meta:    
        model = Category
        fields = ["id", "name", "image", "slug", "featured"]

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "image", "slug", "github", "demo","featured"] 