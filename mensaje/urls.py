from django.urls import path
from .views import MensajeView

urlpatterns = [
    path("mensajes/", MensajeView.as_view(), name="mensajes-list"),
    path("mensajes/<int:pk>/", MensajeView.as_view(), name="mensajes-detail")
]