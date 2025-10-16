from django.urls import path

from app.settings.views import CategoryAPIView, ModelProductAPI, ProductAPI

urlpatterns = [
    path("category", CategoryAPIView.as_view(), name='category'),
    path("model", ModelProductAPI.as_view(), name='model'),
    path("product", ProductAPI.as_view(), name='product'),
]


"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
