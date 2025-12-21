from django.urls import path
from .views import CategoryView, ArticleView

urlpatterns = [
    path("category/", CategoryView.as_view(), name="category-list"),
    path("category/<int:pk>/", CategoryView.as_view(), name="category-detail"),
    path("article/", ArticleView.as_view(), name="article-list"),
    path("article/<int:pk>/", ArticleView.as_view(), name="article-detail"),
]