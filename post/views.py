from django.shortcuts import render
from API import SuperAPIView
from .serializers import CategorySerializer, ArticleSerializer
from .models import Category, Article
# Create your views here.
class CategoryView(SuperAPIView):
    model = Category
    serializer = CategorySerializer

class ArticleView(SuperAPIView):
    model = Article
    serializer = ArticleSerializer