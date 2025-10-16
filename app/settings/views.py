from rest_framework.generics import ListAPIView 

from app.settings.models import Category, ModelProduct
from app.settings.serilizers import CategorySerializer, ModelProductSerializer

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ModelProductAPI(ListAPIView):
    queryset = ModelProduct.objects.all()
    serializer_class = ModelProductSerializer