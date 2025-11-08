from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mensaje
from .serializers import MensajeSerializer

def notexist():
    return {"error": "Datos no encontrados"}

class MensajeView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                mensaje = Mensaje.objects.get(pk=pk)
                serializer = MensajeSerializer(mensaje)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Mensaje.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            mensaje = Mensaje.objects.all()
            serializer = MensajeSerializer(mensaje, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            mensaje = Mensaje.objects.get(pk=pk)
        except Mensaje.DoesNotExist:
            return Response(notexist(), status=status.HTTP_404_NOT_FOUND)

        mensaje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        