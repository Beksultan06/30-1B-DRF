from django.urls import path

from app.settings.views import CategoryAPIView, ModelProductAPI

urlpatterns = [
    path("category", CategoryAPIView.as_view(), name='category'),
    path("model", ModelProductAPI.as_view(), name='model'),
]