from django.contrib import admin
from app.settings.models import Category, ModelProduct

@admin.register( Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ModelProduct)
class ModelProductAdmin(admin.ModelAdmin):
    list_display = ['name']