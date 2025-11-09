from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CategorySerializer, ArticleSerializer
from .models import Category, Article
# Create your views here.

# funcion notexits para el 404
def notexist():
    return {"error": "Los datos no fueron encontrados"}

class CategoryView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try: 
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ArticleView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                article = Article.objects.get(pk=pk)
                serializer = ArticleSerializer(article)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Article.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            article = Article.objects.all()
            serializer = ArticleSerializer(article, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUNDº)
        
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)