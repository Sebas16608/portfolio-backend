from django.shortcuts import render
from .models import Mensaje
from .serializers import MensajeSerializer
from API import SuperAPIView
# Create your views here.
class MensajeView(SuperAPIView):
    model = Mensaje
    serializer = MensajeSerializer
