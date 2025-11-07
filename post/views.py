from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CategorySerializer, ArticleSerializer
from .models import Category, Article
# Create your views here.

# funcion notexits para el 404
def notexist():
    return {"erro": "Los datos no fueron encontrados"}

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
        
                
