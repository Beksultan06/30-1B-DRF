from rest_framework import serializers
from app.settings.models import Category, ModelProduct

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        mdoel = Category
        fields = ['id', 'name']

class ModelProductSerializer(serializers.ModelSerializer):
    class Metya:
        model = ModelProduct
        fields = ['id', 'name']

        