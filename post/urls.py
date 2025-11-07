from .views import CategoryView, ArticleView
from django.urls import path

urlpatterns = [
    path("category/", CategoryView.as_view(), name="categoria-list"),
    path("category/<int:pk>/", CategoryView.as_view(), name="category-detail"),
    path("article/", ArticleView.as_view(), name="articulo-list"),
    path("article/<int:pk>/", ArticleView.as_view(), name="articulo-detail")
]