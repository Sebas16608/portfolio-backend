from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def notexist():
    return {"error": "Los datos no fueron encontrados"}

class SuperAPIView(APIView):
    model = None
    serializer = None

    def get(self, request, pk=None):
        if pk:
            try:
                obj = self.model.object.get(pk=pk)
                serializer = self.serializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except self.model.DoesNotExist:
                return Response(notexist(), status=status.HTTP_404_NOT_FOUND)
        else:
            obj = self.model.object.all()
            serializer = self.serializer(obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)