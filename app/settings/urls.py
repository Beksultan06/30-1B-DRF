from django.urls import path

from app.settings.views import (
    CategoryAPIView, ModelProductAPI, ProductAPI, CategoryCreateAPIView,
    CategoryUpdateAPIView, CategoryDetailAPIView, CategoryDeleteAPIView
)

urlpatterns = [
    path("category", CategoryAPIView.as_view(), name='category'),
    path("category-create", CategoryCreateAPIView.as_view(), name='create-category'),
    path("category-update/<int:pk>/", CategoryUpdateAPIView.as_view(), name='category-update'),
    path("category-detail/<int:pk>/", CategoryDetailAPIView.as_view(), name='category-detail'),
    path("category-delete/<int:pk>/", CategoryDeleteAPIView.as_view(), name='category-delete'),
    path("model", ModelProductAPI.as_view(), name='model'),
    path("product", ProductAPI.as_view(), name='product'),
]


"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
