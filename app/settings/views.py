from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView,\
RetrieveAPIView, DestroyAPIView

from app.settings.models import Category, ModelProduct, Product
from app.settings.serilizers import CategorySerializer, ModelProductSerializer,\
ProductSerializer

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ModelProductAPI(ListAPIView):
    queryset = ModelProduct.objects.all()
    serializer_class = ModelProductSerializer

class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

